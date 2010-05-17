from django import forms
from news21national.core.models import Profile
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import RadioSelect

from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Row, HTML

from news21national.core.constants import GENDERS

class ProfileForm(forms.ModelForm):
	birthdate = forms.DateTimeField(label="Birthdate", required=True, widget=SelectDateWidget(years=range(2010, 1920, -1)))
	expected_grad_date = forms.DateTimeField(label="Expected Date of Graduation", required=True, widget=SelectDateWidget())
	gender = forms.CharField(label="Gender", required=True, widget=RadioSelect(choices=(GENDERS)))
	
	helper = FormHelper()

	layout = Layout(
		Fieldset('Biography Info',
			'blog_uri',
			'twitterid',
			'twitter_public',
			'linkedinid',
			'linkedin_public',
			'facebookid',
			'facebook_public',
			'bio',
			css_class='inlineLabels',),

		Fieldset('Personal Info', 
			'non_edu_email',
			'phone',
			'hometown',
			'address',
			'address_city',
			'address_state',
			'address_zip',
			'birthdate',
			'ethnicity',
			'gender',
			css_class='inlineLabels',),

		Fieldset('Collegiate/Career Info',	
			'expected_grad_date',
			'school',
			'year_in_school',
			'degree_area',
			'desired_job',
			css_class='inlineLabels',)
	)

	helper.add_layout(layout)


	submit = Submit('update','Update Profile')
	helper.add_input(submit)

	class Meta:
		model = Profile
		exclude = ('user','created_at','created_by','updated_at','updated_by','is_active')