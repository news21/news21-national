from django.db import models
import django.contrib.auth.models as auth
from django import forms
from tagging.fields import TagField
from tagging.models import Tag
from datetime import datetime

class NewsOrganization(models.Model):
	name = models.CharField(max_length=150)
	site_url = models.URLField(verify_exists=True,verbose_name="Site URL")
	shorter_code = models.CharField(max_length=10,null=True,blank=True)
	bio = models.TextField()
	created_by = models.ForeignKey(auth.User, related_name="newsorganization_created_by")
	created_at = models.DateTimeField(editable=False)
	updated_by = models.ForeignKey(auth.User, related_name="newsorganization_updated_by")
	updated_at = models.DateTimeField(editable=False)

	def __unicode__(self):
		return unicode(self.name)

	def __str__(self):
		return self.name

	def save(self):
		if self.created_at == None:
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			super(NewsOrganization, self).save()

class Newsroom(models.Model):    
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=150)
    site_url = models.URLField(verify_exists=True,verbose_name="Site URL")
    shorter_code = models.CharField(max_length=10,null=True,blank=True)
    bio = models.TextField()
    is_active = models.BooleanField(default=True)
    members = models.ManyToManyField(auth.User, related_name="newsroom_members",null=True,blank=True)
    created_by = models.ForeignKey(auth.User, related_name="newsroom_created_by")
    created_at = models.DateTimeField(editable=False)
    updated_by = models.ForeignKey(auth.User, related_name="newsroom_updated_by")
    updated_at = models.DateTimeField(editable=False)
    organization = models.ForeignKey(NewsOrganization, related_name="newsroom_newsorganization",null=True,blank=True)
    tags = TagField()


    def __unicode__(self):
        return unicode(self.name)

    def __str__(self):
        return self.name

    def save(self):
        if self.created_at == None:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        super(Newsroom, self).save()

	def get_absolute_url(self):
		return "/newsroom/%s/" % unicode(self.id)

    def set_tags(self, tags):
        Tag.objects.update_tags(self, tags)

    def get_tags(self):
        return Tag.objects.get_for_object(self)