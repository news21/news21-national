from datetime import datetime
from django.db import models
from django.conf import settings

from news21national.multimedia.models import Media, MediaManager

class LinkManager(MediaManager):
    pass

class Link(Media):

    url = models.URLField(verify_exists=True,verbose_name="Media Link URL")
    objects = LinkManager()