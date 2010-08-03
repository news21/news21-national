from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns ('',

    url(r'member/add/$','news21national.partner.views.create_partner_member',name='partner_create_member',),
    url(r'dashboard/$','news21national.partner.views.dashboard',name='partner_dashboard',),
    url(r'generate_apikey/(?P<partner_id>\d+)/$','news21national.partner.views.generate_api_key',name='partner_generate_api_key',),
	url(r'stories/newsroom/(?P<newsroom_id>\d+)/$','news21national.partner.views.filter_stories_by_newsroom',name='partner_filter_stories_by_newsroom',),
	url(r'stories/reporter/(?P<reporter_id>\d+)/$','news21national.partner.views.filter_stories_by_reporter',name='partner_filter_stories_by_reporter',),
	url(r'stories/tag/(?P<tag_name>.+)/$','news21national.partner.views.filter_stories_by_tag',name='partner_filter_stories_by_tag',),
	url(r'stories/year/(?P<year>\d+)/$','news21national.partner.views.filter_stories_by_year',name='partner_filter_stories_by_year',),
	url(r'stories/budget/(?P<story_id>\d+)/$','news21national.partner.views.story_budget',name='partner_story_budget',),
	url(r'stories/metabudget/(?P<metastory_id>\d+)/$','news21national.partner.views.metastory_budget',name='partner_metastory_budget',),
	
	url(r'newsroom/(?P<newsroom_id>\d+)/bios/$','news21national.core.views.get_newsroom_roster',{'template':'partner/bios.html'},name='partner_filter_bios_by_newsroom',),
	url(r'bio/(?P<reporter_id>\d+)/$','news21national.core.views.get_reporter_bio',{'template':'partner/bios.html'},name='partner_filter_bios_by_reporter',),

)