from django.db import models
import django.contrib.auth.models as auth
from django.forms import ModelForm
from datetime import datetime
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _

class Award(models.Model):
	name = models.CharField(max_length=150,verbose_name="Name Of Award")
	presented_by = models.CharField(max_length=150,verbose_name="Presented By")
	presented_at = models.DateTimeField(verbose_name="Presented On")
	
	content_type = models.ForeignKey(ContentType, related_name="content_type_set_for_%(class)s")
	object_id = models.PositiveIntegerField(_('object ID'), max_length=50)
	object = generic.GenericForeignKey('content_type', 'object_id')
	
	members = models.ManyToManyField(auth.User, related_name="award_members",null=True,blank=True)
	created_by = models.ForeignKey(auth.User, related_name="award_created_by")
	created_at = models.DateTimeField(editable=False)
	updated_by = models.ForeignKey(auth.User, related_name="award_updated_by")
	updated_at = models.DateTimeField(editable=False)
	
	def __unicode__(self):
		return unicode(self.name)

	def __str__(self):
		return self.name

	def save(self):
		if self.created_at == None:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		super(Award, self).save()