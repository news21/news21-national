from django import template
from django.conf import settings
from news21national.photos.models import Photo

register = template.Library()

def render_photo(id):
	return '<img src="%s" />' % (Photo.objects.get(pk=id).img_url)

def render_thumb_with_link(id):
	try: 
		p = Photo.objects.get(pk=id)
		r ='<a href="%s" target="_blank"><img src="%s" /></a>' % (p.img_url, p.thumb_url)
	except Photo.DoesNotExist:
		r = ''
	return r
	
register.simple_tag(render_photo)
register.simple_tag(render_thumb_with_link)