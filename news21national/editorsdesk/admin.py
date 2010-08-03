from django.contrib import admin
from news21national.editorsdesk.models import EditorsDesk

admin.site.register(EditorsDesk)

class EditorsDeskAdmin(admin.ModelAdmin):
	pass