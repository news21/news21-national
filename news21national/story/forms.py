from django import forms
from news21national.story.models import MetaStory, Story, StoryPublishDate
from news21national.newsroom.models import Newsroom

from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import Select
from news21national.story.constants import STAGE_CHOICES, STAGE_DEFAULT
from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Row, HTML

class MetaStoryForm(forms.ModelForm):
	newsrooms = forms.ModelMultipleChoiceField(queryset = Newsroom.objects.extra(select={'shorter_year': 'CAST(shorter_code AS INTEGER)'}).order_by('-shorter_year','name'))
	helper = FormHelper()

	layout = Layout(
		Fieldset('',
			'project','newsrooms','headline','slug','original_url','summary','process','interest',
			css_class='inlineLabels',),
	)

	helper.add_layout(layout)

	class Meta:
		model = MetaStory
		exclude = ('is_active','sub_headline','status','primary_image','secondary_image','created_at','created_by','updated_at','updated_by','tags','stage')


class StoryForm(forms.ModelForm):
	helper = FormHelper()

	layout = Layout(
		Fieldset('',
			'headline','slug','original_url','summary','process',
			css_class='inlineLabels',),
	)

	helper.add_layout(layout)
	
	class Meta:
		model = Story
		exclude = ('metastory','sort','status','authors','created_at','created_by','updated_at','updated_by','tags','primary_image','secondary_image','stage')

class StoryPublishDateForm(forms.ModelForm):
	available_at = forms.DateTimeField(label="Start Date", required=False, widget=SelectDateWidget(years=range(2010, 2000, -1)))
	expires_at = forms.DateTimeField(label="End Date", required=False, widget=SelectDateWidget(years=range(2010, 2000, -1)))

	helper = FormHelper()

	layout = Layout(
		Fieldset('',
			'title','available_at','expires_at',
			css_class='inlineLabels',),
	)

	helper.add_layout(layout)

	class Meta:
		model = StoryPublishDate
		exclude = ('story','created_at','created_by','updated_at','updated_by')