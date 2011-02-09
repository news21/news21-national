from django.contrib import admin
from news21national.plaintext.models import PlainText

class PlainTextAdmin(admin.ModelAdmin):
	list_display = ('id', 'title','summary','status')
	list_filter = ['status', ]
	search_fields = ['title','summary']

admin.site.register(PlainText,PlainTextAdmin)
