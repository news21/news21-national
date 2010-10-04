from django.db import models
import django.contrib.auth.models as auth
from django.forms import ModelForm
from datetime import datetime
from news21national.story.models import Story
from news21national.api.models import Key

class Partner(models.Model):
	name = models.CharField(max_length=150,verbose_name="Media Outlet Name")
	site_url = models.URLField(verify_exists=True,verbose_name="Site URL")
	phone = models.CharField(max_length=25,verbose_name="Contact Phone",null=True,blank=True)
	email = models.EmailField(max_length=150,verbose_name="Contact Email",null=True,blank=True)
	members = models.ManyToManyField(auth.User, related_name="partner_members",null=True,blank=True)
	created_by = models.ForeignKey(auth.User, related_name="partner_created_by")
	created_at = models.DateTimeField(editable=False)
	updated_by = models.ForeignKey(auth.User, related_name="partner_updated_by")
	updated_at = models.DateTimeField(editable=False)
	
	def __unicode__(self):
		return unicode(self.name)

	def __str__(self):
		return self.name
	
	def get_keys(self):
		return Key.objects.get_for_object(self)

	def add_key(self,user):
		return Key.objects.add_key(self,user)
		
	def save(self):
		if self.created_at == None:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		super(Partner, self).save()
		


class StoryPlacements(models.Model):
	partner = models.ForeignKey(Partner)
	story = models.ForeignKey(Story)
	placement_headline = models.CharField(max_length=200,verbose_name="Partner Headline",null=True,blank=True)
	description = models.CharField(max_length=200,verbose_name="Description")
	story_ran = models.DateTimeField()
	placement_url = models.URLField(verify_exists=False,verbose_name="Placement URL",null=True,blank=True)
	screengrab_url = models.URLField(verify_exists=False,verbose_name="Screengrab URL",null=True,blank=True)
	url_active = models.BooleanField(default=True)
	created_by = models.ForeignKey(auth.User, related_name="storyplacement_created_by")
	created_at = models.DateTimeField(editable=False)
	updated_by = models.ForeignKey(auth.User, related_name="storyplacement_updated_by")
	updated_at = models.DateTimeField(editable=False)

	def save(self):
		if self.created_at == None:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		super(StoryPlacements, self).save()