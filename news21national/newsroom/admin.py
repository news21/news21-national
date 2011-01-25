from django.contrib import admin
from news21national.newsroom.models import Newsroom, NewsOrganization
from news21national.core.models import Profile
from django import forms

class NewsOrganizationAdmin(admin.ModelAdmin):
	list_display = ('name','shorter_code','site_url')

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'created_by':
			kwargs['initial'] = request.user.id
			return db_field.formfield(**kwargs)
		if db_field.name == 'updated_by':
			kwargs['initial'] = request.user.id
			return db_field.formfield(**kwargs)
		return super(NewsOrganizationAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class NewsroomForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(NewsroomForm, self).__init__(*args, **kwargs)
		profiles = Profile.objects.all();
		s = self.fields['members'].widget
		choices = []
		for choice in profiles:
			choices.append((choice.id, '('+choice.school+') '+choice.first_name+ ' '+choice.last_name+' ( '+str(choice.user.email)+' )' ))
		s.choices = sorted(choices, key=lambda c: c[1])

class NewsroomAdmin(admin.ModelAdmin):
	form = NewsroomForm
	list_display = ('name','site_url','shorter_code','organization','is_active')

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