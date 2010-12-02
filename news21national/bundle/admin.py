from django.contrib import admin
from news21national.bundle.models import StoryBundle
from news21national.story.models import Story
from tagging.models import Tag
from news21national.newsroom.models import Newsroom
from django import forms
import datetime

class StoryBundleForm(forms.ModelForm):	
	def __init__(self, *args, **kwargs):
		super(StoryBundleForm, self).__init__(*args, **kwargs)
		stories = Story.objects.all();
		s = self.fields['stories'].widget
		choices = []
		for choice in stories:
			choices.append((choice.id, '( '+str(choice.created_at.year)+': '+choice.newsrooms+' ) '+choice.headline+' ( '+choice.metastory.headline+' ) '))
		s.choices = choices

class StoryBundleAdmin(admin.ModelAdmin):
	form = StoryBundleForm
	
	def change_view(self, request, object_id, extra_context=None):
		my_context = {
			'tags': Tag.objects.all(),
			'newsrooms': Newsroom.objects.all(),
		}
		return super(StoryBundleAdmin, self).change_view(request, object_id,extra_context=my_context)

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'created_by':
			kwargs['initial'] = request.user.id
			return db_field.formfield(**kwargs)
		if db_field.name == 'updated_by':
			kwargs['initial'] = request.user.id
			return db_field.formfield(**kwargs)
		return super(StoryBundleAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(StoryBundle,StoryBundleAdmin)