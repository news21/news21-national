from django import template
from django.conf import settings
from news21national.photos.models import Photo

register = template.Library()

def render_photo(id):
	return '<img src="%s" />' % (Photo.objects.get(pk=id).img_url)
	
register.simple_tag(render_photo)