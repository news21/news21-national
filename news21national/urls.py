
from django.conf.urls.defaults import patterns, include, handler500, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

handler500 # Pyflakes

urlpatterns = patterns(
    '',
    url(r'^$', 'news21national.core.views.home', name='home'),
    (r'^admin/(.*)', admin.site.root),
    
    (r'^account/', include('django_authopenid.urls')),
    
    url(r'^accounts/profile/', 'news21national.core.views.user_profile',  name='user_profile'),
    url(r'^accounts/association/', 'news21national.core.views.user_association',  name='user_association'),
    url(r'^dashboard/', 'news21national.core.views.dashboard',  name='user_dashboard'),
    url(r'^privacy/', 'news21national.core.views.privacy',  name='privacy'),
	url(r'^terms/', 'news21national.core.views.terms',  name='terms'),
    
    (r'^editorsdesk/',include('news21ams.editorsdesk.urls')),
    (r'^newsroom/',include('news21ams.newsroom.urls')),
    (r'^partner/',include('news21ams.partner.urls')),
    (r'^builder/',include('news21ams.story.urls')),
    (r'^api/',include('news21ams.api.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
         {'document_root': settings.MEDIA_ROOT}),
    )
