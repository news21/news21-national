from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns ('',

	url(r'dashboard/$','news21national.editorsdesk.views.dashboard',name='editorsdesk_dashboard',),
	url(r'dashboard/analytics$','news21national.editorsdesk.views.analytics',name='editorsdesk_analytics',),
	url(r'dashboard/analytics/report-alllast30days$','news21national.editorsdesk.views.report_alllast30days',name='editorsdesk_analytics_report_alllast30days',),
	url(r'dashboard/analytics/report-firstxmonths$','news21national.editorsdesk.views.report_firstxmonths',name='editorsdesk_analytics_report_firstxmonths',),
	url(r'dashboard/analytics/report-daterange$','news21national.editorsdesk.views.report_daterange',name='editorsdesk_analytics_report_daterange',),
	
	url(r'review/package/(?P<metastory_id>\d+)$','news21national.story.views.get_metastory', {'template_name':'story/metastory.html'}, name='editorsdesk_review_metastory',),
	url(r'review/package/(?P<metastory_id>\d+)/story/(?P<story_id>\d+)$','news21national.story.views.get_story', {'template_name':'story/story.html'}, name='editorsdesk_review_story',),
	url(r'review/plaintext/(?P<multimedia_id>\d+)$','news21national.plaintext.views.edit_plaintext', {'template_name':'multimedia/plaintext.html'}, name='editorsdesk_review_plaintext',),
	url(r'review/package/(?P<metastory_id>\d+)/story/(?P<story_id>\d+)/photo/(?P<multimedia_id>\d+)$','news21national.photos.views.get_photo', {'template_name':'multimedia/photo.html'}, name='editorsdesk_review_photo',),
	url(r'review/audio/(?P<multimedia_id>\d+)$','news21national.audio.views.get_audio', {'template_name':'multimedia/audio.html'}, name='editorsdesk_review_audio',),
	
	url(r'review/package/(?P<metastory_id>\d+)/status$','news21national.editorsdesk.views.review_metastory', name='editorsdesk_update_status_metastory',),
	url(r'review/package/(?P<metastory_id>\d+)/story/(?P<story_id>\d+)/status$','news21national.editorsdesk.views.review_story', name='editorsdesk_update_status_story',),
	url(r'review/multimedia/(?P<multimedia_id>\d+)/status$','news21national.editorsdesk.views.review_multimedia', name='editorsdesk_update_status_multimedia'),

)
