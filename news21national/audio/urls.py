from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns ('news21national.audio.views',

    url(r'^$','get_audio',name='audio_new'),
    url(r'^create/$','save_audio',name='audio_create'),
    url(r'^(?P<multimedia_id>\d+)/$','get_audio',name='audio_edit'),
    url(r'^(?P<multimedia_id>\d+)/update/$','save_audio',name='audio_update'),

)