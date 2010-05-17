from django.contrib import admin
from news21national.core.models import Profile

admin.site.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('username')