from datetime import datetime
from django.db import models
import django.contrib.auth.models as auth
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _

class CodeRepoManager(models.Manager):
    def get_for_object(self, obj):
        """
        Returns the repoz associated with the given object or None.
        """
        ctype = ContentType.objects.get_for_model(obj)
        try:
            return self.filter(content_type=ctype, object_id=obj.pk)
        except ObjectDoesNotExist:
            pass
        return []

class CodeRepo(models.Model):
	content_type = models.ForeignKey(ContentType, related_name="content_type_set_for_%(class)s")
	object_id = models.PositiveIntegerField(_('object ID'), max_length=50)
	object = generic.GenericForeignKey('content_type', 'object_id')

	title = models.CharField(max_length=200)
	description = models.TextField()
	code = models.FileField(_('code'), upload_to='uploads/coderepo/%Y/%m/%d', max_length=255, null=True, blank=True)
	code_url = models.URLField(verify_exists=False,verbose_name="Code Repository URL",null=True,blank=True)
	created_by = models.ForeignKey(auth.User, related_name="coderepo_created_by")
	created_at = models.DateTimeField(editable=False)
	updated_by = models.ForeignKey(auth.User, related_name="coderepo_updated_by")
	updated_at = models.DateTimeField(editable=False)
	
	objects = CodeRepoManager()
	
	def __unicode__(self):
		return unicode(self.title)

	def __str__(self):
		return self.title

	def save(self):
		if self.created_at == None:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		super(CodeRepo, self).save()