from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns ('news21national.story.views',

    url(r'^package/$','get_metastory',name='metastory_new'),
    url(r'^package/create/$','save_metastory',name='metastory_create'),
    url(r'^package/(?P<metastory_id>\d+)/$','get_metastory',name='metastory_edit'),
    url(r'^package/(?P<metastory_id>\d+)/update/$','save_metastory',name='metastory_update'),
    
    url(r'^package/(?P<metastory_id>\d+)/story/$','get_story',name='story_new'),
    url(r'^package/(?P<metastory_id>\d+)/story/create/$','save_story',name='story_create'),
    url(r'^package/(?P<metastory_id>\d+)/story/(?P<story_id>\d+)/$','get_story',name='story_edit'),
    url(r'^package/(?P<metastory_id>\d+)/story/(?P<story_id>\d+)/update/$','save_story',name='story_update'),
    
    url(r'^package/(?P<metastory_id>\d+)/story/(?P<story_id>\d+)/publishdate/create/$','save_publishdate',name='storypublishdate_create'),
    url(r'^package/(?P<metastory_id>\d+)/story/(?P<story_id>\d+)/publishdate/delete/$','remove_publishdate',name='storypublishdate_update'),

    (r'^package/(?P<metastory_id>\d+)/story/(?P<story_id>\d+)/assets/',include('news21national.multimedia.urls')),
)
