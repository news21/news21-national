from django.contrib import admin
from news21national.awards.models import Award

class AwardAdmin(admin.ModelAdmin):
	list_display = ('name','presented_by','presented_at')

admin.site.register(Award,AwardAdmin)