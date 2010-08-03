from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns ('',

	url(r'(?P<newsroom_id>\d+)/member/add/$','news21national.newsroom.views.create_newsroom_member',name='newsroom_create_member',),

)
