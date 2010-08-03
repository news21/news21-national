from datetime import datetime
from django.db import models
from django.conf import settings

from news21national.multimedia.models import Media, MediaManager

class EmbedManager(MediaManager):
    pass

class Embed(Media):

    content = models.TextField(blank=False,verbose_name="Embed Code")
    objects = EmbedManager()