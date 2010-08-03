from django.db import models
import django.contrib.auth.models as auth
from django import forms
from datetime import datetime
from news21national.multimedia.models import Media
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _

class Outlet(models.Model):	   
	name = models.CharField(max_length=150)
	site_url = models.URLField(verify_exists=True,verbose_name="Site URL")
	username = models.CharField(max_length=150)
	tags = models.CharField(max_length=150)
	
	def __unicode__(self):
		return unicode(self.name)

	def __str__(self):
		return self.name

class PayloadManager(models.Manager):
    def get_for_object(self, obj, outlet):
        ctype = ContentType.objects.get_for_model(obj)
        try:
            return self.get(content_type=ctype, object_id=obj.pk, outlet=outlet)
        except:
            pass
        return None

class Payload(models.Model):
	content_type = models.ForeignKey(ContentType, related_name="content_type_set_for_%(class)s")
	object_id = models.PositiveIntegerField(_('object ID'), max_length=50)
	object = generic.GenericForeignKey('content_type', 'object_id')
	
	outlet = models.ForeignKey(Outlet)
	title = models.CharField(max_length=100,blank=True,null=True)
	blurb = models.TextField(null=True,blank=True)
	placement_url = models.CharField(max_length=400,null=True,blank=True)
	placed_by = models.ForeignKey(auth.User, related_name="socialpayload_placed_by",null=True,blank=True)
	placed_at = models.DateTimeField(editable=False,null=True,blank=True)
	created_by = models.ForeignKey(auth.User, related_name="socialpayload_created_by")
	created_at = models.DateTimeField(editable=False)
	updated_by = models.ForeignKey(auth.User, related_name="socialpayload_updated_by")
	updated_at = models.DateTimeField(editable=False)
	
	objects = PayloadManager()
	
	def __unicode__(self):
		return unicode(self.media.title)

	def __str__(self):
		return self.media.title

	def save(self):
		if self.created_at == None:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		super(Payload, self).save()

class Scheduler(models.Model):
	payload = models.ForeignKey(Payload)
	created_by = models.ForeignKey(auth.User, related_name="socialscheduler_created_by")