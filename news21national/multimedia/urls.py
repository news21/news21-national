from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns ('news21national.multimedia.views',

    (r'^plaintext/',include('news21national.plaintext.urls')),
    (r'^photo/',include('news21national.photos.urls')),
    (r'^audio/',include('news21national.audio.urls')),
    (r'^embed/',include('news21national.embed.urls')),
    (r'^video/',include('news21national.videos.urls')),

)
