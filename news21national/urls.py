
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
	
	url(r'^roster/(?P<newsroom_id>\d+)/', 'news21national.core.views.get_newsroom_roster',  name='user_newsroom_roster'),
	url(r'bio/(?P<reporter_id>\d+)/$','news21national.core.views.get_reporter_bio',{'template':'core/bio.html'},name='user_bio',),
	url(r'urls/$','news21national.story.views.get_story_shorturls',name='short_urls',),
	
	url(r'^dashboard/', 'news21national.core.views.dashboard',	name='user_dashboard'),
	
	(r'^editorsdesk/',include('news21national.editorsdesk.urls')),
	(r'^partner/',include('news21national.partner.urls')),
	
	(r'^bundle/',include('news21national.bundle.urls')),
	(r'^newsroom/',include('news21national.newsroom.urls')),
	(r'^builder/',include('news21national.story.urls')),
	(r'^api/',include('news21national.api.urls')),
	
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
