from django.conf import settings
from django.conf.urls.defaults import *

from news21national.videos.forms import VideoForm

urlpatterns = patterns ('news21national.videos.views',

	url(r'^$','get_video',name='video_new'),
	url(r'^create/$','save_video',name='video_create'),
	url(r'^(?P<multimedia_id>\d+)/$','get_video',name='video_edit'),
	url(r'^(?P<multimedia_id>\d+)/update/$','save_video',name='video_update'),

)