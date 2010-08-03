from django.contrib import admin
from news21national.plaintext.models import PlainText

class PlainTextAdmin(admin.ModelAdmin):
	pass

admin.site.register(PlainText)
