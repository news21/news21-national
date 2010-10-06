from django import template
from django.conf import settings
from news21national.core.models import Profile

register = template.Library()

def render_bio(id):
	return 'bio'

	
register.simple_tag(render_bio)