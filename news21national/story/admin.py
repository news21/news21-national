from django.contrib import admin
from news21national.story.models import MetaStory,Story

admin.site.register(MetaStory)
admin.site.register(Story)

class MetaStoryAdmin(admin.ModelAdmin):
	pass

class StoryAdmin(admin.ModelAdmin):
	pass