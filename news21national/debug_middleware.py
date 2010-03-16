#
# http://www.djangosnippets.org/snippets/1872/
#
import time
from django.test.signals import template_rendered
from django.conf import settings
from django.db import connection
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

TEMPLATE = """
<div id="debug" style="clear:both;">
<a href="#debugbox"
    onclick="this.style.display = 'none';
        document.getElementById('debugbox').style.display = 'block';
        return false;"
    style="font-size: small; color: red; text-decoration: none; display: block; margin: 12px;"
>+</a>

<div style="display: none;clear: both; border: 1px solid red; padding: 12px; margin: 12px; overflow: scroll; white-space: wrap;" id="debugbox">

<p>Server-time taken: {{ server_time|floatformat:"5" }} seconds</p>
<p>View: <strong>{{view}}</strong></p>
<p>Templates used:</p>
{% if templates %}
<ol>
    {% for template in templates %}
        <li><strong>{{ template.0 }}</strong> loaded from <samp>{{ template.1 }}</samp></li>
    {% endfor %}
</ol>
{% else %}
    None
{% endif %}
<p>Template path:</p>
{% if template_dirs %}
    <ol>
    {% for template in template_dirs %}
        <li>{{ template }}</li>
    {% endfor %}
    </ol>
{% else %}
    <ul><li>None</li></ul>
{% endif %}
<p>SQL executed:</p>
{% if sql %}
<ol>
{% for query in sql %}
    <li{{ query.style }}>{{ query.sql|linebreaksbr }}
        <p>took {{ query.time|floatformat:"3" }} seconds</p>{{ query.count }}</li>
{% endfor %}
</ol>
<p>Total SQL time: {{ sql_total }} in {{num_queries}} queries</p>
{% else %}
    None
{% endif %}
</div>
</div>
</body>
"""

# Monkeypatch instrumented test renderer from django.test.utils - we could use
# django.test.utils.setup_test_environment for this but that would also set up
# e-mail interception, which we don't want
from django.test.utils import instrumented_test_render
from django.template import Template, Context
if Template.render != instrumented_test_render:
    Template.original_render = Template.render
    Template.render = instrumented_test_render
# MONSTER monkey-patch
old_template_init = Template.__init__
def new_template_init(self, template_string, origin=None, name='<Unknown Template>'):
    old_template_init(self, template_string, origin, name)
    self.origin = origin
Template.__init__ = new_template_init

class DebugFooter:
    def process_request(self, request):
        self.time_started = time.time()
        self.templates_used = []
        self.contexts_used = []
        self.sql_offset_start = len(connection.queries)
        template_rendered.connect(self._storeRenderedTemplates)

    def process_response(self, request, response):
        # Only include debug info for text/html pages not accessed via Ajax
        if 'text/html' not in response['Content-Type']:
            return response
        if request.is_ajax():
            return response
        if not settings.DEBUG:
            return response
        if response.status_code != 200:
            return response

        templates = []
        for t in self.templates_used:
            if t.origin and t.origin.name:
                templates.append( (t.name, _txtmate(t.origin.name,t.origin.name) ) )
            else:
                templates.append( (t.name, "no origin") )

        sql_queries = connection.queries[self.sql_offset_start:]
        # Reformat sql queries a bit
        sql_total = 0.0
        sql_counts = {}
        for query in sql_queries:
            raw_sql = query['sql']
            query['sql'] = reformat_sql(query['sql'])
            sql_total += float(query['time'])
            count = sql_counts.get(raw_sql,0) + 1
            sql_counts[raw_sql] = count
            if count > 1:
                query['style'] = mark_safe(' style="background:#ff0000;"')
                query['count'] = mark_safe('<p>duplicate query count=%s</p>' % count)
            else:
                query['style'] = ''
                query['count'] = ''

        from django.core.urlresolvers import resolve
        view_func, args, kwargs = resolve(request.META['PATH_INFO']) #@UnusedVariable

        view =  '%s.%s' % (view_func.__module__, view_func.__name__)

        vf = view_func
        breaker = 10
        while not hasattr(vf,'func_code'):
            if hasattr(vf,'view_func'):
                vf = vf.view_func
            else:
                break # somethings wrong about the assumptions of the decorator
            breaker = breaker - 1
            if breaker < 0:
                break
        if hasattr(vf,'func_code'):
            co = vf.func_code
            filename = co.co_filename
            lineno = co.co_firstlineno
            view = _txtmate(co.co_filename,view,co.co_firstlineno)

        debug_content = Template(TEMPLATE).render(Context({
            'server_time': time.time() - self.time_started,
            'templates': templates,
            'sql': sql_queries,
            'sql_total': sql_total,
            'num_queries' : len(sql_queries),
            'template_dirs': settings.TEMPLATE_DIRS,
            'view': view
        }))

        content = response.content
        response.content = force_unicode(content).replace('</body>', debug_content)

        return response

    def _storeRenderedTemplates(self, **kwargs):
        #signal=signal, sender=sender, template=template, context=context):
        template = kwargs.get('template')
        if(template):
            self.templates_used.append(template)
        context = kwargs.get('context')
        if(context):
            self.contexts_used.append(context)


def reformat_sql(sql):
    sql = sql.replace('`,`', '`, `')
    sql = sql.replace('` FROM `', '` \n  FROM `')
    sql = sql.replace('` WHERE ', '` \n  WHERE ')
    sql = sql.replace(' ORDER BY ', ' \n  ORDER BY ')
    return sql

def _txtmate(path,name,lineno=""):
    return mark_safe("<a href='txmt://open/?url=file://%s&amp;line=%s'>%s</a>" % (path,lineno,name))
