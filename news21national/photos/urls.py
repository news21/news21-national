from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns ('news21national.photos.views',

    url(r'^$','get_photo',name='photo_new'),
    url(r'^create/$','save_photo',name='photo_create'),
    url(r'^(?P<multimedia_id>\d+)/$','get_photo',name='photo_edit'),
    url(r'^(?P<multimedia_id>\d+)/update/$','save_photo',name='photo_update'),

)