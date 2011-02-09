from django.contrib import admin
from news21national.embed.models import Embed

class EmbedAdmin(admin.ModelAdmin):
	list_display = ('title','story','status')
	list_filter = ['status', ]
	search_fields = ['title','summary']

admin.site.register(Embed,EmbedAdmin)
