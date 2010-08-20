def site_style(request):
	from django.conf import settings
	return {'SITE_STYLE': settings.SITE_STYLE}