from django.contrib import admin
from news21national.story.models import MetaStory,Story

admin.site.register(MetaStory)

class MetaStoryAdmin(admin.ModelAdmin):
	pass

class StoryAdmin(admin.ModelAdmin):	
	list_display = ('id','headline','metastory','status')
	
admin.site.register(Story,StoryAdmin)