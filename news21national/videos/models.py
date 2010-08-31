from datetime import datetime

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.db import models

from news21national.multimedia.models import Media, MediaManager

class VideoManager(MediaManager):
	pass

class Video(Media):
	video = models.FileField(_('video'), upload_to='uploads/video/%Y/%m/%d', max_length=255,blank=True,null=True)
	hq_file = models.CharField(max_length=255,blank=True,null=True)
	date_taken = models.DateTimeField(null=True)
	duration = models.PositiveIntegerField(blank=True,null=True)
	cuepoints = models.TextField(blank=True,null=True)
	objects = VideoManager()