from django import forms
from news21national.core.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user','gender','created_at','created_by','updated_at','updated_by')
