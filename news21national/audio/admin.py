from django.contrib import admin
from news21national.audio.models import Audio

class AudioAdmin(admin.ModelAdmin):
	list_display = ('id', 'title','status')
	list_filter = ['status', ]
	search_fields = ['title','summary']

admin.site.register(Audio,AudioAdmin)