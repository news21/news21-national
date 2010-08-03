from datetime import datetime

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.db import models

from news21national.multimedia.models import Media, MediaManager

class AudioManager(MediaManager):
    pass

class Audio(Media):

    audio = models.FileField(_('audio'), upload_to='uploads/audio/%Y/%m/%d', max_length=255)
    objects = AudioManager()