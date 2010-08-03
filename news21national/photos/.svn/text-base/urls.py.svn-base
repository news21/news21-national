from django.conf import settings
from django.conf.urls.defaults import *
from photos.models import Gallery, Photo

# Number of random images from the gallery to display.
SAMPLE_SIZE = ":%s" % getattr(settings, 'GALLERY_SAMPLE_SIZE', 5)

# galleries

urlpatterns = patterns('',
    url(r'^gallery/(?P<media_id>\d+)/(?P<slug>[\-\d\w]+)/$', 
        'photos.views.gallery_detail', 
         name='photos_gallery_detail'),

    url(r'^gallery/page/(?P<page>[0-9]+)/$', 
        'django.views.generic.list_detail.object_list', 
        {'queryset': Gallery.objects.published(), 
         'allow_empty': True, 
         'paginate_by': 5, 
         'extra_context':{'sample_size':SAMPLE_SIZE}}, 
        name='photos_gallery_index'),
)

# photographs
urlpatterns += patterns('',

    url(r'^photo/(?P<media_id>\d+)/json/',
        'photos.views.photo_detail', 
         name='photos_photo_detail_json'),

    url(r'^photo/(?P<media_id>\d+)/(?P<slug>[\-\d\w]+)/$', 
        'photos.views.photo_detail', 
         name='photos_photo_detail'),

    url(r'^photo/page/(?P<page>[0-9]+)/$', 
        'django.views.generic.list_detail.object_list', 
        {'queryset': Photo.objects.published(), 
         'allow_empty': True, 
         'paginate_by': 20, 
         'extra_context':{'sample_size':SAMPLE_SIZE}}, 
        name='photos_photo_index'),
)


