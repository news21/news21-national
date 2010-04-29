
from django.conf.urls.defaults import patterns, include, handler500, url
from django.conf import settings as asettings
from mobileadmin.conf import settings
from django.contrib import admin

from news21national.core.forms import ProfileForm

admin.autodiscover()

import mobileadmin
mobileadmin.autoregister()

#handler500 # Pyflakes
handler404 = 'mobileadmin.views.page_not_found'
handler500 = 'mobileadmin.views.server_error'

urlpatterns = patterns(
	'',
	url(r'^$', 'news21national.core.views.home', name='home'),
	(r'^admin/(.*)', admin.site.root),
	(r'^ma/(.*)', mobileadmin.sites.site.root),
	
	(r'^account/', include('django_authopenid.urls')),
	
	url(r'^accounts/profile/update/$', 'news21national.core.views.save_profile',	 name='save_profile'),
	url(r'^accounts/profile/$', 'news21national.core.views.user_profile',  name='user_profile'),
	url(r'^accounts/profile/validate/$', 'ajax_validation.views.validate', {'form_class': ProfileForm}, 'validate_user_profile'),
	
	
	url(r'^accounts/association/', 'news21national.core.views.user_association',  name='user_association'),
	
	url(r'^dashboard/', 'news21national.core.views.dashboard',	name='user_dashboard'),
	url(r'^privacy/', 'news21national.core.views.privacy',	name='privacy'),
	url(r'^terms/', 'news21national.core.views.terms',	name='terms'),
	
	(r'^editorsdesk/',include('news21ams.editorsdesk.urls')),
	(r'^newsroom/',include('news21ams.newsroom.urls')),
	(r'^partner/',include('news21ams.partner.urls')),
	(r'^builder/',include('news21ams.story.urls')),
	(r'^api/',include('news21ams.api.urls')),
	(r'^messages/', include('django_messages.urls')),
	(r"^announcements/", include("announcements.urls")),
	(r'^avatar/', include('avatar.urls')),
)

if asettings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': asettings.MEDIA_ROOT}),
		(settings.MEDIA_REGEX, 'django.views.static.serve', {'document_root': settings.MEDIA_PATH}),
	)
