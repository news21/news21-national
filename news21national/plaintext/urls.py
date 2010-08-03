from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns ('news21national.plaintext.views',

    url(r'^$','new_plaintext',name='plaintext_new'),
    url(r'^create/$','save_plaintext',name='plaintext_create'),
    url(r'^(?P<multimedia_id>\d+)/$','edit_plaintext',name='plaintext_edit'),
    url(r'^(?P<multimedia_id>\d+)/update/$','save_plaintext',name='plaintext_update'),
    
)
