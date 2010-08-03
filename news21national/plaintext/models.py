from django.db import models
from news21national.multimedia.models import Media, MediaManager

class PlainTextManager(MediaManager):
    pass
    
class PlainText(Media):
    content = models.TextField(blank=False)
    
    objects = PlainTextManager()