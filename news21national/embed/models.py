from datetime import datetime
from django.db import models
from django.conf import settings

from news21national.embed.constants import THRIDPARTY_CHOICES
from news21national.multimedia.models import Media, MediaManager

class EmbedManager(MediaManager):
    pass

class Embed(Media):

    content = models.TextField(blank=False,verbose_name="Embed Code")
    thirdparty = models.CharField(max_length=50, choices = THRIDPARTY_CHOICES,null=True,blank=True,verbose_name="Type",)
    objects = EmbedManager()