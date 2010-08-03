from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns ('',

    url(r'(?P<slug>.+)/$','news21national.bundle.views.get_bundle',name='bundles_bundle',),

)