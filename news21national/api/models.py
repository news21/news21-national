from datetime import datetime
from django.db import models
import django.contrib.auth.models as auth
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
import md5, random, sys
from django.conf import settings

class KeyManager(models.Manager):
	def get_for_object(self, obj):
		"""
		Returns the api keys associated with the given object or None.
		"""
		ctype = ContentType.objects.get_for_model(obj)
		try:
			return self.filter(content_type=ctype, object_id=obj.pk, is_active=True)
		except ObjectDoesNotExist:
			pass
		return []

	def add_key(self, obj, user):
		"""
		Associate an API key to an object.
		"""
		ctype = ContentType.objects.get_for_model(obj)
		hashkey = md5.new(str(random.randint(0, sys.maxint - 1)) + settings.SECRET_KEY).hexdigest() + str(ctype.id) + str(obj.id)
		
		Key._default_manager.create(content_type=ctype, object_id=obj.id, api_key=hashkey, created_by=user, updated_by=user)

class Key(models.Model):
	content_type = models.ForeignKey(ContentType, related_name="content_type_set_for_%(class)s")
	object_id = models.PositiveIntegerField(_('object ID'), max_length=50)
	object = generic.GenericForeignKey('content_type', 'object_id')

	api_key = models.CharField(max_length=100,editable=False,null=True,blank=True)
	is_active = models.BooleanField(default=True)
	created_by = models.ForeignKey(auth.User, related_name="apikey_created_by")
	created_at = models.DateTimeField(editable=False)
	updated_by = models.ForeignKey(auth.User, related_name="apikey_updated_by")
	updated_at = models.DateTimeField(editable=False)
	
	objects = KeyManager()
	
	def __unicode__(self):
		return unicode(self.api_key)

	def __str__(self):
		return self.api_key

	def save(self, force_insert=False, force_update=False):
		if self.created_at == None:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		super(Key, self).save()