from django.contrib import admin
from news21national.links.models import Link

class LinkAdmin(admin.ModelAdmin):
	list_display = ('title','url')

admin.site.register(Link,LinkAdmin)