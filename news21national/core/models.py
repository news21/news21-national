from django.db import models
import django.contrib.auth.models as auth
from django.forms import ModelForm
from datetime import datetime
from news21national.core.constants import ETHNICITIES,DEGREE_TYPES,DEGREE_AREAS,SCHOOLS


class Profile(models.Model):
	user = models.ForeignKey(auth.User)
	phone = models.CharField(max_length=25,blank=True,verbose_name="Mobile #")
	gender = models.CharField(max_length=10,default=False)
	blog_uri = models.CharField(max_length=300,blank=True,verbose_name="Personal Website/Blog URL")
	twitterid = models.CharField(max_length=200,blank=True,verbose_name="Twitter Username")
	twitter_public = models.BooleanField(default=False,verbose_name="Show Twitter Username in Public Profile?")
	linkedinid = models.CharField(max_length=200,blank=True,verbose_name="LinkedIn Username")
	linkedin_public = models.BooleanField(default=False,verbose_name="Show LinkedIn Username in Public Profile?")
	facebookid = models.CharField(max_length=200,blank=True,verbose_name="Facebook Username")
	facebook_public = models.BooleanField(default=False,verbose_name="Show Facebook Username in Public Profile?")
	bio = models.TextField(help_text="Exclude school details, which will be inherited from below fields.")
	hometown = models.CharField(max_length=100)
	address = models.CharField(max_length=200,help_text="E.g.: La Messa Drive 1234")
	address_city = models.CharField(max_length=200,verbose_name="City")
	address_state = models.CharField(max_length=40,verbose_name="State")
	address_zip = models.CharField(max_length=20,verbose_name="Zip")
	birthdate = models.DateTimeField()
	expected_grad_date = models.DateTimeField()
	non_edu_email = models.CharField(max_length=200)
	ethnicity = models.CharField(max_length=40,choices=ETHNICITIES,default='Other')
	year_in_school = models.CharField(max_length=40,choices=DEGREE_TYPES,default='Other')
	school = models.CharField(max_length=60,choices=SCHOOLS)
	degree_area = models.CharField(max_length=40,choices=DEGREE_AREAS,default='Other')
	desired_job = models.CharField(max_length=100,blank=True,null=True)
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