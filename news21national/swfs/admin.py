from django.contrib import admin
from news21national.swfs.models import Swf

class SwfAdmin(admin.ModelAdmin):
	list_display = ('title','story','status')
	list_filter = ['status', ]
	search_fields = ['title','summary']

admin.site.register(Swf,SwfAdmin)
