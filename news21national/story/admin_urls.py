from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns ('news21national.story.admin_views',
	url(r'^filtered/(?P<filter_name>.+)/$', 'filtered', name='admin_story_filters'),
)

