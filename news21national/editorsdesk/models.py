from django.db import models
import django.contrib.auth.models as auth
from django.forms import ModelForm
from datetime import datetime
from news21national.newsroom.models import Newsroom

class EditorsDesk(models.Model):
	newsroom =	models.ForeignKey(Newsroom)
	editors = models.ManyToManyField(auth.User, related_name="editorsdesk_editors",null=True,blank=True)
	created_by = models.ForeignKey(auth.User, related_name="editorsdesk_created_by")
	created_at = models.DateTimeField(editable=False)
	updated_by = models.ForeignKey(auth.User, related_name="editorsdesk_updated_by")
	updated_at = models.DateTimeField(editable=False)
	
	def __unicode__(self):
		return unicode(self.newsroom.short_name)

	def __str__(self):
		return self.newsroom.short_name

	def save(self):
		if self.created_at == None:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		super(EditorsDesk, self).save()
