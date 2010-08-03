from django.contrib import admin
from news21national.socialchecklist.models import Outlet

admin.site.register(Outlet)

class OutletAdmin(admin.ModelAdmin):
	list_display = ('name','username')