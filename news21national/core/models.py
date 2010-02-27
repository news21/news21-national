from django.db import models
import django.contrib.auth.models as auth
from django.forms import ModelForm

# add photo
class Profile(models.Model):
	user = models.ForeignKey(auth.User)
	phone = models.CharField(max_length=25,blank=True)
	gender = models.BooleanField(default=True)
	blog_uri = models.CharField(max_length=300)
	twitterid = models.CharField(max_length=200)
	linkedinid = models.CharField(max_length=200)
	facebookid = models.CharField(max_length=200)
	bio = models.TextField()

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		exclude = ('user',)

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