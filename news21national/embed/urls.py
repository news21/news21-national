from django.conf import settings
from django.conf.urls.defaults import *

from news21national.embed.forms import EmbedForm

urlpatterns = patterns ('news21national.embed.views',

	url(r'^$','get_embed',name='embed_new'),
	url(r'^create/$','save_embed',name='embed_create'),
	url(r'^(?P<multimedia_id>\d+)/$','get_embed',name='embed_edit'),
	url(r'^(?P<multimedia_id>\d+)/update/$','save_embed',name='embed_update'),
#	url(r'^validate/$', 'ajax_validation.views.validate', {'form_class': EmbedForm}, name='validate_embed'),
)