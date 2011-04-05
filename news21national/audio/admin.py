from django.contrib import admin
from news21national.audio.models import Audio
from django import forms
from news21national.story.models import Story

class AudioFormAdmin(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(AudioFormAdmin, self).__init__(*args, **kwargs)
		wtf = Story.objects.all();
		s = self.fields['story'].widget
		choices = []
		for choice in wtf:
			choices.append((choice.id, '( '+str(choice.created_at.year)+': '+choice.newsrooms+' ) '+choice.headline+ ' By: '+choice.story_authors ))
		s.choices = sorted(choices, key=lambda c: c[1])

class AudioAdmin(admin.ModelAdmin):
	form = AudioFormAdmin
	list_display = ('id', 'title','status')
	list_filter = ['status', ]
	search_fields = ['title','summary']

admin.site.register(Audio,AudioAdmin)