from django.contrib import admin
from news21national.videos.models import Video

class VideoAdmin(admin.ModelAdmin):
	list_display = ('id', 'title','hq_file','status')
	
admin.site.register(Video,VideoAdmin)
