from django.contrib import admin
from news21national.partner.models import Partner, StoryPlacements, MetaStoryPlacements
from news21national.story.models import MetaStory, Story
from django import forms
import datetime


class PartnerAdmin(admin.ModelAdmin):
	ordering = ('name',)
	list_display = ('name','site_url','phone','email')
	search_fields = ['name']

admin.site.register(Partner,PartnerAdmin)

class StoryPlacementsForm(forms.ModelForm):
	
	def __init__(self, *args, **kwargs):
		super(StoryPlacementsForm, self).__init__(*args, **kwargs)
		wtf = Story.objects.all();
		s = self.fields['story'].widget
		choices = []
		for choice in wtf:
			choices.append((choice.id, '( '+str(choice.created_at.year)+': '+choice.newsrooms+' ) '+choice.headline+ ' By: '+choice.story_authors ))
		s.choices = sorted(choices, key=lambda c: c[1])

class StoryPlacementsAdmin(admin.ModelAdmin):
	form = StoryPlacementsForm
	list_display = ('story','partner')

admin.site.register(StoryPlacements,StoryPlacementsAdmin)



class MetaStoryPlacementsForm(forms.ModelForm):
	
	def __init__(self, *args, **kwargs):
		super(MetaStoryPlacementsForm, self).__init__(*args, **kwargs)
		wtf = MetaStory.objects.all();
		s = self.fields['metastory'].widget
		choices = []
		for choice in wtf:
			choices.append((choice.id, '( '+str(choice.created_at.year)+': '+choice.metastory_newsrooms+' ) '+choice.headline ))
		s.choices = sorted(choices, key=lambda c: c[1])


class MetaStoryPlacementsAdmin(admin.ModelAdmin):
	form = MetaStoryPlacementsForm
	list_display = ('metastory','partner')

admin.site.register(MetaStoryPlacements,MetaStoryPlacementsAdmin)