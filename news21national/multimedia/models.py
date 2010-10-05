from django.db import models
import django.contrib.auth.models as auth
from datetime import datetime

from tagging.fields import TagField
from tagging.models import Tag
import geotagging
from geotagging.models import Geotag

from news21national.utils.model_inheritance import ParentModel,ChildManager
from news21national.multimedia.constants import LICENSE_CHOICES, LICENSE_DEFAULT, STATUS_CHOICES, STATUS_DEFAULT, STAGE_DEFAULT, STAGE_CHOICES
from news21national.story.models import Story
from news21national.core.models import Profile

class MediaManager(models.Manager):
	pass
	
class Media(ParentModel):
	story = models.ForeignKey(Story)
	title = models.CharField(max_length=128)
	status = models.CharField(max_length=20, choices = STATUS_CHOICES, default=STATUS_DEFAULT,)
	stage = models.CharField(max_length=50, choices = STAGE_CHOICES, default=STAGE_DEFAULT,null=True,blank=True,)
	summary = models.TextField(blank=False)
	authors = models.ManyToManyField(auth.User, related_name="media_authors")
	slug = models.SlugField(unique=True)
	attribution = models.TextField(blank=True)
	is_active = models.BooleanField(default=True)
	license = models.CharField(max_length=100, choices = LICENSE_CHOICES, default=LICENSE_DEFAULT,)
	pub_date = models.DateTimeField(editable=False,null=True)
	created_by = models.ForeignKey(auth.User, related_name="media_created_by")
	created_at = models.DateTimeField(editable=False)
	updated_by = models.ForeignKey(auth.User, related_name="media_updated_by")
	updated_at = models.DateTimeField(editable=False)
	tags = TagField()


	objects = MediaManager()
	children = ChildManager()
	
	def __unicode__(self):
		return unicode(self.title)

	def __str__(self):
		return self.title

	def save(self):
		if self.created_at == None:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		super(Media, self).save()

	def _set_tags(self, tags):
		Tag.objects.update_tags(self, tags)

	def _get_tags(self):
		return Tag.objects.get_for_object(self)

	def _get_geotag(self):
		return Geotag.objects.get_for_object(self)

	def _remove_geotag(self):
		geotag_obj = Geotag.objects.get_for_object(self)
		if geotag_obj is not None:
			geotag_obj.delete()

	def get_authors(self):
		return Profile.objects.filter(user__in=self.authors.values_list('id',flat=True)).distinct().order_by('last_name')
	media_authors = property(get_authors)
	
	def get_parent_model(self):
		"""
		Helper method for inheritance
		"""
		return Media

geotagging.register(Media)