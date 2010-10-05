import urllib

from django import template
from django.utils.translation import ugettext as _
from django.utils.hashcompat import md5_constructor
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from django.conf import settings
from news21national.core.models import Profile

register = template.Library()

def render_byline(user):
	
	return 'a'
	
register.simple_tag(render_byline)