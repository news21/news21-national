from django.contrib import admin
from news21national.plaintext.models import PlainText

class PlainTextAdmin(admin.ModelAdmin):
	list_display = ('id', 'title','summary','status')
	list_filter = ['status', ]

admin.site.register(PlainText,PlainTextAdmin)
