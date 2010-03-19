from django import template
from django.utils.safestring import mark_safe, SafeData
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag
@stringfilter
def ga_title_monthyear(value):
	l = value.split('|')
	m = 0
	y = 0
	for t in l:
		if(t.split('=')[0] == 'ga:month')
			m = t.split('=')[1]
		if(t.split('=')[0] == 'ga:year')
			y = t.split('=')[1]
	r = datetime.date(y, m, 1).strftime("%b %y") if m > 0 and y > 0 else ""
	return r