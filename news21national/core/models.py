from django.db import models
import django.contrib.auth.models as auth
from django.forms import ModelForm

class Profile(models.Model):
    user = models.ForeignKey(auth.User)
    phone = models.CharField(max_length=25,blank=True)

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
