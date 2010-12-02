from django.contrib import admin
from news21national.links.models import Link

class LinkAdmin(admin.ModelAdmin):
	list_display = ('title','url','status')
	list_filter = ['status', ]

admin.site.register(Link,LinkAdmin)