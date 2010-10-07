from django.db import models
import django.contrib.auth.models as auth
from news21national.newsroom.models import Newsroom
from news21national.story.models import Story
from tagging.fields import TagField
from tagging.models import Tag
from datetime import datetime

class StoryBundle(models.Model):
	title = models.CharField(max_length=200,null=True,blank=True)
	slug = models.SlugField(unique=True,help_text="<a class='helptip'>What's this? Shorten it!</a>")
	stories = models.ManyToManyField(Story)
	created_by = models.ForeignKey(auth.User, related_name="bundles_created_by")
	created_at = models.DateTimeField(editable=False)
	updated_by = models.ForeignKey(auth.User, related_name="bundles_updated_by")
	updated_at = models.DateTimeField(editable=False)

	def __unicode__(self):
		return unicode(self.title)

	def __str__(self):
		return self.title

	def save(self):
		if self.created_at == None:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		super(StoryBundle, self).save()

	def _set_tags(self, tags):
		Tag.objects.update_tags(self, tags)

	def _get_tags(self):
		return Tag.objects.get_for_object(self)