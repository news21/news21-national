from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns ('news21national.swfs.views',

    url(r'^$','get_swf',name='swf_new'),
    url(r'^create/$','save_swf',name='swf_create'),
    url(r'^(?P<multimedia_id>\d+)/$','get_swf',name='swf_edit'),
    url(r'^(?P<multimedia_id>\d+)/update/$','save_swf',name='swf_update'),

)