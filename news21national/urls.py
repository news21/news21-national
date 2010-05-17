
from django.conf.urls.defaults import patterns, include, handler500, url
from django.conf import settings as settings

from django.contrib import admin

from news21national.core.forms import ProfileForm

admin.autodiscover()

urlpatterns = patterns(
	'',
	url(r'^$', 'news21national.core.views.home', name='home'),
	('^admin/', include(admin.site.urls)),
	
	(r'^account/', include('django_authopenid.urls')),
	
	url(r'^accounts/profile/update/$', 'news21national.core.views.save_profile',	 name='save_profile'),
	url(r'^accounts/profile/$', 'news21national.core.views.user_profile',  name='user_profile'),
	url(r'^accounts/profile/validate/$', 'ajax_validation.views.validate', {'form_class': ProfileForm}, 'validate_user_profile'),
	url(r'^accounts/association/', 'news21national.core.views.user_association',  name='user_association'),
	url(r'^accounts/pending/', 'news21national.core.views.user_accountpending',  name='user_accountpending'),
	
	url(r'^dashboard/', 'news21national.core.views.dashboard',	name='user_dashboard'),
	
	(r'^editorsdesk/',include('news21ams.editorsdesk.urls')),
	(r'^newsroom/',include('news21ams.newsroom.urls')),
	(r'^partner/',include('news21ams.partner.urls')),
	(r'^builder/',include('news21ams.story.urls')),
	(r'^api/',include('news21ams.api.urls')),
	(r'^messages/', include('django_messages.urls')),
	(r"^announcements/", include("announcements.urls")),
	(r'^avatar/', include('avatar.urls')),
	
	url(r'^preview/(?P<page_id>\d+)/', 'feincms.views.base.preview_handler', name='feincms:preview'),
	url(r'^$', 'feincms.views.base.handler', { 'path': '/home' }),
	url(r'^$|^(.*)/$', 'feincms.views.base.handler'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
		
		(r'^feincms_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.FEINCMS_ADMIN_MEDIA}),
	)
