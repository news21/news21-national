from django.contrib import admin
from news21national.awards.models import Award
from django.contrib.contenttypes.models import ContentType
from news21national.newsroom.models import Newsroom

class AwardAdmin(admin.ModelAdmin):
	list_display = ('name','presented_by','presented_at')
	'''
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'content_type':
			kwargs['queryset'] = ContentType.objects.filter(name__in=['project','meta story','story'])
			return db_field.formfield(**kwargs)
		return super(AwardAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
	'''
	def change_view(self, request, object_id, extra_context=None):
		my_context = {
			'newsrooms': Newsroom.objects.all(),
		}
		return super(AwardAdmin, self).change_view(request, object_id,extra_context=my_context)
	
	def add_view(self, request, extra_context=None):
		my_context = {
			'newsrooms': Newsroom.objects.all(),
		}
		return super(AwardAdmin, self).add_view(request,extra_context=my_context)

admin.site.register(Award,AwardAdmin)