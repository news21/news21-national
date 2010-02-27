from django.db import models
import django.contrib.auth.models as auth
from django.forms import ModelForm
from datetime import datetime

# add photo
class Profile(models.Model):
	user = models.ForeignKey(auth.User)
	phone = models.CharField(max_length=25,blank=True)
	gender = models.BooleanField(default=True)
	blog_uri = models.CharField(max_length=300,blank=True)
	twitterid = models.CharField(max_length=200,blank=True)
	linkedinid = models.CharField(max_length=200,blank=True)
	facebookid = models.CharField(max_length=200,blank=True)
	bio = models.TextField()
	created_by = models.ForeignKey(auth.User, related_name="profile_created_by")
	created_at = models.DateTimeField(editable=False)
	updated_by = models.ForeignKey(auth.User, related_name="profile_updated_by")
	updated_at = models.DateTimeField(editable=False)

	def save(self):
		if self.created_at == None:
			self.created_at = datetime.now()
		self.updated_at = datetime.now()
		super(Profile, self).save()

class Skill(models.Model):
	title = models.CharField(max_length=200)

class UserSkills(models.Model):
	user = models.ForeignKey(auth.User)
	skill = models.ForeignKey(Skill)
	sort = models.IntegerField()
	created_by = models.ForeignKey(auth.User, related_name="userskill_created_by")
	created_at = models.DateTimeField(editable=False)

class UserSuggestedLeads(models.Model):
	user = models.ForeignKey(auth.User)
	oulet = models.CharField(max_length=200)
	outlet_uri = models.CharField(max_length=300)
	outlet_phone = models.CharField(max_length=25,blank=True)
	created_by = models.ForeignKey(auth.User, related_name="usersuggestedleads_created_by")
	created_at = models.DateTimeField(editable=False)