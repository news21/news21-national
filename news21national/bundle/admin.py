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

	def save_model(self, request, obj, form, change): 
			instance = form.save(commit=False)
			if not hasattr(instance, 'created_by'):
				instance.created_by = request.user
			instance.modified_by = request.user
			instance.save()
			form.save_m2m()
			return instance

	def save_formset(self, request, form, formset, change): 
		def set_user(instance):
			if not hasattr(instance, 'created_by'):
				instance.created_by = request.user
			instance.modified_by = request.user
			instance.save()

		if formset.model == User:
			instances = formset.save(commit=False)
			map(set_user, instances)
			formset.save_m2m()
			return instances
		else:
			return formset.save()



admin.site.register(StoryBundle,StoryBundleAdmin)