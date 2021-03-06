def site_style(request):
	from django.conf import settings
	return {'SITE_STYLE': settings.SITE_STYLE}
def api_version(request):
	from django.conf import settings
	return {'API_VERSION': settings.API_VERSION}
def internal_api_key(request):
	from django.conf import settings
	return {'INTERNAL_API_KEY': settings.INTERNAL_API_KEY}
def site_domain(request):
	from django.conf import settings
	return {'SITE_DOMAIN': settings.SITE_DOMAIN}
def default_avatar(request):
	from django.conf import settings
	return {'DEFAULT_AVATAR': settings.MEDIA_URL+''+settings.AVATAR_DEFAULT_URL}