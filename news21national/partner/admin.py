from django.contrib import admin
from news21national.partner.models import Partner, StoryPlacements
from news21national.story.models import MetaStory, Story
from django import forms
import datetime

admin.site.register(Partner)

class PartnerAdmin(admin.ModelAdmin):
	pass


class StoryPlacementsForm(forms.ModelForm):	
	def __init__(self, *args, **kwargs):
		super(StoryPlacementsForm, self).__init__(*args, **kwargs)
		wtf = Story.objects.all();
		s = self.fields['story'].widget
		choices = []
		for choice in wtf:
			choices.append((choice.id, '( '+str(choice.created_at.year)+': '+choice.newsrooms+' ) '+choice.headline))
		s.choices = choices


class StoryPlacementsAdmin(admin.ModelAdmin):
	form = StoryPlacementsForm

admin.site.register(StoryPlacements,StoryPlacementsAdmin)