from django.contrib import admin
from news21national.partner.models import Partner, StoryPlacements

admin.site.register(Partner)
admin.site.register(StoryPlacements)

class PartnerAdmin(admin.ModelAdmin):
	pass

class StoryPlacementsAdmin(admin.ModelAdmin):
	pass