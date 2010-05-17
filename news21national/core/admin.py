from django.contrib import admin
from news21national.core.models import Profile


class ProfileAdmin(admin.ModelAdmin):
	list_display = ['first_name','last_name','is_active',]
	list_filter = ['is_active',]
	ordering = ['last_name',]
	search_fields = ['first_name','last_name',]

admin.site.register(Profile, ProfileAdmin)