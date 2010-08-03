from django.contrib import admin
from news21national.newsroom.models import Newsroom

admin.site.register(Newsroom)

class NewsroomAdmin(admin.ModelAdmin):
	list_display = ('name','short_name','is_active')