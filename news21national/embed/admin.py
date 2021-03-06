from django.contrib import admin
from news21national.embed.models import Embed
from django import forms
from news21national.story.models import Story

class EmbedFormAdmin(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(EmbedFormAdmin, self).__init__(*args, **kwargs)
		wtf = Story.objects.all();
		s = self.fields['story'].widget
		choices = []
		for choice in wtf:
			choices.append((choice.id, '( '+str(choice.created_at.year)+': '+choice.newsrooms+' ) '+choice.headline+ ' By: '+choice.story_authors ))
		s.choices = sorted(choices, key=lambda c: c[1])
		
class EmbedAdmin(admin.ModelAdmin):
	form = EmbedFormAdmin
	list_display = ('title','story','status')
	list_filter = ['status', ]
	search_fields = ['title','summary']

admin.site.register(Embed,EmbedAdmin)
