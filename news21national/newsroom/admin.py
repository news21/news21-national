from django.contrib import admin
from news21national.newsroom.models import Newsroom, NewsOrganization


class NewsOrganizationAdmin(admin.ModelAdmin):
	list_display = ('name','site_url')

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'created_by':
			kwargs['initial'] = request.user.id
			return db_field.formfield(**kwargs)
		if db_field.name == 'updated_by':
			kwargs['initial'] = request.user.id
			return db_field.formfield(**kwargs)
		return super(NewsOrganizationAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class NewsroomAdmin(admin.ModelAdmin):
	list_display = ('name','short_name','shorter_code','is_active')

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'created_by':
			kwargs['initial'] = request.user.id
			return db_field.formfield(**kwargs)
		if db_field.name == 'updated_by':
			kwargs['initial'] = request.user.id
			return db_field.formfield(**kwargs)
		return super(NewsroomAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
		

admin.site.register(Newsroom, NewsroomAdmin)
admin.site.register(NewsOrganization, NewsOrganizationAdmin)