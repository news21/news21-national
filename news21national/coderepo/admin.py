from django.contrib import admin
from news21national.coderepo.models import CodeRepo

admin.site.register(CodeRepo)

class CodeRepoAdmin(admin.ModelAdmin):
	list_display = ('title','description')