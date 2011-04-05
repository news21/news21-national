from django.contrib import admin
from news21national.links.models import Link
from django import forms
from news21national.story.models import Story

class LinkFormAdmin(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(LinkFormAdmin, self).__init__(*args, **kwargs)
		wtf = Story.objects.all();
		s = self.fields['story'].widget
		choices = []
		for choice in wtf:
			choices.append((choice.id, '( '+str(choice.created_at.year)+': '+choice.newsrooms+' ) '+choice.headline+ ' By: '+choice.story_authors ))
		s.choices = sorted(choices, key=lambda c: c[1])

class LinkAdmin(admin.ModelAdmin):
	form = LinkFormAdmin
	list_display = ('thirdparty','title','url','status')
	list_filter = ['status', ]
	search_fields = ['title','summary']

admin.site.register(Link,LinkAdmin)