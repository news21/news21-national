from django.contrib import admin
from news21national.story.models import MetaStory,Story,Project

from news21national.awards.models import Award
from django.contrib.contenttypes import generic

class AwardInline(generic.GenericTabularInline):
		model = Award

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('id','admin_image','admin_screenshot','started_at','name','description')
	search_fields = ['name','description']
	inlines = [AwardInline,]

class MetaStoryAdmin(admin.ModelAdmin):
	list_display = ('id','headline','project','summary','status')
	list_filter = ['status','newsrooms']
	search_fields = ['headline','sub_headline','summary','process']
	inlines = [AwardInline,]

class StoryAdmin(admin.ModelAdmin): 
	list_display = ('id','headline','metastory','status','newsroom_year')
	list_filter = ['status','metastory']
	search_fields = ['headline','summary','process']
	inlines = [AwardInline,]

admin.site.register(Project,ProjectAdmin)
admin.site.register(MetaStory,MetaStoryAdmin)
admin.site.register(Story,StoryAdmin)

