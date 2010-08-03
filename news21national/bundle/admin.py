from django.contrib import admin
from news21national.bundle.models import StoryBundle

admin.site.register(StoryBundle)

class StoryBundleAdmin(admin.ModelAdmin):
	pass