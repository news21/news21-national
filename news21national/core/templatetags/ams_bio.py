from django import template
from django.conf import settings
from news21national.core.models import Profile

register = template.Library()

def render_bio(id):
	return 'bio'

def render_fullname(id):
	try: 
		profile = Profile.objects.get(user=id)
		r = profile.first_name+' '+profile.last_name
	except Profile.DoesNotExist:
		r = ''
	return r

def render_school(id):
	try: 
		profile = Profile.objects.get(user=id)
		r = profile.school
	except Profile.DoesNotExist:
		r = ''
	return r

register.simple_tag(render_bio)
register.simple_tag(render_fullname)
register.simple_tag(render_school)