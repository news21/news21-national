from datetime import datetime
from django.db import models
from django.conf import settings

from news21national.links.constants import THRIDPARTY_CHOICES
from news21national.multimedia.models import Media, MediaManager

class LinkManager(MediaManager):
    pass

class Link(Media):

    url = models.URLField(verify_exists=True,verbose_name="Media Link URL")
    thirdparty = models.CharField(max_length=50, choices = THRIDPARTY_CHOICES,null=True,blank=True,verbose_name="Type",)
    objects = LinkManager()