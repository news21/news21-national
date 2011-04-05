from django.contrib import admin
from news21national.videos.models import Video
from django import forms
from news21national.story.models import Story

class VideoFormAdmin(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(VideoFormAdmin, self).__init__(*args, **kwargs)
		wtf = Story.objects.all();
		s = self.fields['story'].widget
		choices = []
		for choice in wtf:
			choices.append((choice.id, '( '+str(choice.created_at.year)+': '+choice.newsrooms+' ) '+choice.headline+ ' By: '+choice.story_authors ))
		s.choices = sorted(choices, key=lambda c: c[1])

class VideoAdmin(admin.ModelAdmin):
	form = VideoFormAdmin
	list_display = ('id', 'title','hq_file','status')
	list_filter = ['status', ]
	search_fields = ['title','summary']
	
admin.site.register(Video,VideoAdmin)
