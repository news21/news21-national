from django.db import models
import django.contrib.auth.models as auth
from django.forms import ModelForm
from datetime import datetime
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _

class AwardManager(models.Manager):
	def get_for_object(self, obj):
		ctype = ContentType.objects.get_for_model(obj)
		return self.filter(content_type__pk=ctype.pk,object_id=obj.pk)

	def get_for_user(self, user):
		return self.filter(members=user.id)

class Award(models.Model):
	name = models.CharField(max_length=150,verbose_name="Name Of Award")
	presented_by = models.CharField(max_length=150,verbose_name="Presented By")
	presented_at = models.DateTimeField(verbose_name="Presented On")
	presented_url = models.URLField(verify_exists=False,verbose_name="Presented By URL",null=True,blank=True)
	
	content_type = models.ForeignKey(ContentType, related_name="content_type_set_for_%(class)s")
	object_id = models.PositiveIntegerField(_('object ID'), max_length=50)
	object = generic.GenericForeignKey('content_type', 'object_id')
	
	members = models.ManyToManyField(auth.User, related_name="award_members",null=True,blank=True)
	created_by = models.ForeignKey(auth.User, related_name="award_created_by")
	created_at = models.DateTimeField(editable=False)
	updated_by = models.ForeignKey(auth.User, related_name="award_updated_by")
	updated_at = models.DateTimeField(editable=False)
	
	objects = AwardManager()
	
	def __unicode__(self):
		return unicode(self.name)

	def __str__(self):
		return self.name

	def save(self):
		if self.created_at == None:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		super(Award, self).save()