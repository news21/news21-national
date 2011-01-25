from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns ('',
	url(r'^v1/(?P<api_key>.+)/categories/(?P<dif>.+)/$','news21national.api.views.story_categories',{'version':'v1'},name='api_topics',),
	url(r'v1/(?P<api_key>.+)/category/(?P<category_id>.+)/stories/(?P<dif>.+)/$','news21national.api.views.stories_by_category',{'version':'v1'},name='api_topicstories',),
	url(r'v1/(?P<api_key>.+)/story/(?P<story_id>\d+)/(?P<dif>.+)/$','news21national.api.views.story',name='api_story',),
	url(r'v1/(?P<api_key>.+)/story_ec/(?P<story_id>\d+)/(?P<dif>.+)/$','news21national.api.views.story',{'version':'v1','custom_filter':'_ec'},name='api_story_ec',),
	url(r'v1/(?P<api_key>.+)/newsrooms/(?P<dif>.+)/$','news21national.api.views.newsrooms_categories',{'version':'v1'},name='api_newsrooms',),
	url(r'v1/(?P<api_key>.+)/newsroom/(?P<newsroom_id>\d+)/bios/(?P<dif>.+)/$','news21national.api.views.newsrooms_bios',{'version':'v1'},name='api_newsroom_bios',),
	url(r'v1/(?P<api_key>.+)/filtered_bios/$','news21national.api.views.bios_by_filters',{'version':'v1'},name='api_bios_by_filters',),
	url(r'v1/(?P<api_key>.+)/media/(?P<media_id>\d+)/(?P<dif>.+)/$','news21national.api.views.media',{'version':'v1'},name='api_media',),
	url(r'v1/(?P<api_key>.+)/filtered_stories/$','news21national.api.views.stories_by_filters',{'version':'v1'},name='api_stories_by_filters',),
	url(r'v1/(?P<api_key>.+)/placements/(?P<dif>.+)/$','news21national.api.views.placements',{'version':'v1'},name='api_placements',),
	url(r'v1/(?P<api_key>.+)/organization/(?P<organization_id>\d+)/(?P<dif>.+)/$','news21national.api.views.organizations',{'version':'v1'},name='api_placements',),
	
	url(r'^v2/(?P<api_key>.+)/categories/$','news21national.api.views.story_categories',{'version':'v2'},name='api_topics',),
	url(r'v2/(?P<api_key>.+)/category/(?P<category_id>.+)/stories/$','news21national.api.views.stories_by_category',{'version':'v2'},name='api_topicstories',),
	url(r'v2/(?P<api_key>.+)/story/(?P<story_id>\d+)/$','news21national.api.views.story',{'version':'v2'},name='api_story',),
	url(r'v2/(?P<api_key>.+)/story_ec/(?P<story_id>\d+)/$','news21national.api.views.story',{'version':'v2','custom_filter':'_ec'},name='api_story_ec',),
	url(r'v2/(?P<api_key>.+)/newsrooms/$','news21national.api.views.newsrooms_categories',{'version':'v2'},name='api_newsrooms',),
	url(r'v2/(?P<api_key>.+)/newsroom/(?P<newsroom_id>\d+)/bios/$','news21national.api.views.newsrooms_bios',{'version':'v2'},name='api_newsroom_bios',),
	url(r'v2/(?P<api_key>.+)/filtered_bios/$','news21national.api.views.bios_by_filters',{'version':'v2'},name='api_bios_by_filters',),
	url(r'v2/(?P<api_key>.+)/media/(?P<media_id>\d+)/$','news21national.api.views.media',{'version':'v2'},name='api_media',),
	url(r'v2/(?P<api_key>.+)/filtered_stories/$','news21national.api.views.stories_by_filters',{'version':'v2'},name='api_stories_by_filters',),
	url(r'v2/(?P<api_key>.+)/placements/$','news21national.api.views.placements',{'version':'v2'},name='api_placements',),
	url(r'v2/(?P<api_key>.+)/organization/(?P<organization_id>\d+)/$','news21national.api.views.organizations',{'version':'v2'},name='api_placements',),
)
