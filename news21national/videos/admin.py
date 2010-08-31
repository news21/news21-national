from django.contrib import admin
from news21national.videos.models import Video

class VideoAdmin(admin.ModelAdmin):
	pass

admin.site.register(Video)
