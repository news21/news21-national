import os
import random
import zipfile

from datetime import datetime
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from imagekit.models import ImageModel
from imagekit.lib import Image

from multimedia.models import Media, MediaManager

from django_inlines import inlines

# Modify image file buffer size.
PHOTOS_IMAGEKIT_SPEC = getattr(settings, 'PHOTOS_IMAGEKIT_SPEC', 'photos.ik_specs')


class GalleryManager(MediaManager):
    pass

class Gallery(Media):

    photos = models.ManyToManyField(
                'Photo', 
                related_name='galleries', 
                verbose_name=_('photos'),
                null=True, blank=True)

    objects = GalleryManager()

    def latest(self, limit=0, public=True):
        if limit == 0:
            limit = self.photo_count()
        if public:
            return self.public()[:limit]
        else:
            return self.photos.all()[:limit]

    def sample(self, count=0, public=True):
        if count == 0 or count > self.photo_count():
            count = self.photo_count()
        if public:
            photo_set = self.public()
        else:
            photo_set = self.photos.all()
        return random.sample(photo_set, count)

    def photo_count(self, public=True):
        if public:
            return self.public().count()
        else:
            return self.photos.all().count()
    photo_count.short_description = _('count')

class GalleryUpload(models.Model):
    zip_file = models.FileField(_('images file (.zip)'),
                                upload_to='uploads/photos/tmp',
                                storage=FileSystemStorage(),
                                help_text=_('Select a .zip file of images to upload into a new Gallery.'))
    gallery = models.ForeignKey(Gallery, null=True, blank=True, help_text=_('Select a gallery to add these images to. leave this empty to create a new gallery from the supplied title.'))
    title = models.CharField(_('title'), max_length=75, help_text=_('All photos in the gallery will be given a title made up of the gallery title + a sequential number.'))
    caption = models.TextField(_('caption'), blank=True, help_text=_('Caption will be added to all photos.'))
    description = models.TextField(_('description'), blank=True, help_text=_('A description of this Gallery.'))
    is_public = models.BooleanField(_('is public'), default=True, help_text=_('Uncheck this to make the uploaded gallery and included photographs private.'))

    class Meta:
        verbose_name = _('gallery upload')
        verbose_name_plural = _('gallery uploads')

    def save(self, *args, **kwargs):
        super(GalleryUpload, self).save(*args, **kwargs)
        gallery = self.process_zipfile()
        super(GalleryUpload, self).delete()
        return gallery

    def process_zipfile(self):
        if os.path.isfile(self.zip_file.path):
            # TODO: implement try-except here
            zip = zipfile.ZipFile(self.zip_file.path)
            bad_file = zip.testzip()
            if bad_file:
                raise Exception('"%s" in the .zip archive is corrupt.' % bad_file)
            count = 1
            if self.gallery:
                gallery = self.gallery
            else:
                gallery = Gallery.objects.create(title=self.title,
                                                 title_slug=slugify(self.title),
                                                 description=self.description,
                                                 is_public=self.is_public)
            from cStringIO import StringIO
            for filename in zip.namelist():
                if filename.startswith('__'): # do not process meta files
                    continue
                data = zip.read(filename)
                if len(data):
                    try:
                        # the following is taken from django.newforms.fields.ImageField:
                        #  load() is the only method that can spot a truncated JPEG,
                        #  but it cannot be called sanely after verify()
                        trial_image = Image.open(StringIO(data))
                        trial_image.load()
                        # verify() is the only method that can spot a corrupt PNG,
                        #  but it must be called immediately after the constructor
                        trial_image = Image.open(StringIO(data))
                        trial_image.verify()
                    except Exception, e:
                        # if a "bad" file is found we just skip it.
                        raise e
                        continue
                    while 1:
                        title = ' '.join([self.title, str(count)])
                        slug = slugify(title)
                        try:
                            p = Photo.objects.get(slug=slug)
                        except Photo.DoesNotExist:
                            photo = Photo(title=title,
                                          slug=slug,
                                          caption=self.caption,
                                          is_public=self.is_public)
                            photo.image.save(filename, ContentFile(data))
                            gallery.photos.add(photo)
                            count = count + 1
                            break
                        count = count + 1
            zip.close()
            return gallery


class Image(ImageModel):
    
    crop_horz_choices = (
        (0, 'left'),
        (1, 'center'),
        (2, 'right'),
    )
    crop_vert_choices = (
        (0, 'top'),
        (1, 'center'),
        (2, 'bottom'),
    )
    image = models.ImageField(_('image'), upload_to='uploads/photos/%Y/%m/%d', max_length=255)
    crop_horz = models.PositiveIntegerField(_('crop horizontal'),
                                            choices=crop_horz_choices,
                                            default=1)
    crop_vert = models.PositiveIntegerField(_('crop vertical'),
                                            choices=crop_vert_choices,
                                            default=1)
    view_count = models.PositiveIntegerField(default=0, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.image.name

    class IKOptions:
        spec_module = PHOTOS_IMAGEKIT_SPEC
        save_count_as = 'view_count'
        cache_dir = 'ik_cache/photos'
        cache_filename_format = "%(specname)s/%(filename)s.%(extension)s"
    
class PhotoManager(MediaManager):
    pass

class Photo(Media):

    image = models.ForeignKey(Image)
    created_by = models.ForeignKey(
                        User, 
                        related_name="photos_created")
    modified_by = models.ForeignKey(
                        User, 
                        related_name="photos_modified")
    objects = PhotoManager()

    def get_previous_in_gallery(self, gallery):
        try:
            return self.get_previous_by_date_added(
                        galleries__exact=gallery,)
        except Photo.DoesNotExist:
            return None

    def get_next_in_gallery(self, gallery):
        try:
            return self.get_next_by_date_added(
                        galleries__exact=gallery,)
        except Photo.DoesNotExist:
            return None

    def get_thumbnail_url(self):
        return self.image.mediumthumb.url

    def get_thumbnail_width(self):
        return self.image.mediumthumb.get_width()

    def get_thumbnail30x30_url(self):
        return self.image.thumbnail30x30.url

    def get_display380_url(self):
        return self.image.display380.url
        
    def get_display600_url(self):
        return self.image.display600.url

    def get_display140_url(self):
        return self.image.display140.url

    def get_display940_url(self):
        return self.image.display940.url

    def get_original_url(self):
        return self.image.image.url

    def get_render_url(self):
        return reverse('multimedia_preview', args=[self.id])

    def get_width(self):
        return self.image.image.width

    def get_height(self):
        return self.image.image.height

    def get_inline_code(self):
        """ hack until django_inlines supports this feature """
        return '%s photo %d %s' % (settings.INLINES_START_TAG, 
                                   self.id,
                                   settings.INLINES_END_TAG)

    def get_json_object(self):
        """not used but leaving around for now"""
        return [{ self.id : 
                 { 'display380': self.get_display380_url,
                   'original': self.get_original_url,
                   'title' : self.title, }}]

inlines.registry.register('photo', inlines.inline_for_model(Photo))


