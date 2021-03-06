from django.contrib import admin
from news21national.awards.models import Award
from django.contrib.contenttypes.models import ContentType
from news21national.newsroom.models import Newsroom

class AwardAdmin(admin.ModelAdmin):
	list_display = ('name','presented_by','presented_at')

	def change_view(self, request, object_id, extra_context=None):
		my_context = {
			'newsrooms': Newsroom.objects.extra(select={'shorter_year': 'CAST(shorter_code AS INTEGER)'}).order_by('-shorter_year','name'),
		}
		return super(AwardAdmin, self).change_view(request, object_id,extra_context=my_context)
	
	def add_view(self, request, extra_context=None):
		my_context = {
			'newsrooms': Newsroom.objects.extra(select={'shorter_year': 'CAST(shorter_code AS INTEGER)'}).order_by('-shorter_year','name'),
		}
		return super(AwardAdmin, self).add_view(request,extra_context=my_context)

admin.site.register(Award,AwardAdmin)