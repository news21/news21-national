from django.contrib import admin
from news21national.story.models import MetaStory,Story,Project

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('id','admin_image','started_at','name','description')

class MetaStoryAdmin(admin.ModelAdmin):
	list_display = ('id','headline','project','summary','status')

class StoryAdmin(admin.ModelAdmin):	
	list_display = ('id','headline','metastory','status')
	
admin.site.register(Project,ProjectAdmin)
admin.site.register(MetaStory,MetaStoryAdmin)
admin.site.register(Story,StoryAdmin)