from django.contrib import admin
from news21national.bundle.models import StoryBundle

class StoryBundleAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change): 
			instance = form.save(commit=False)
			if not hasattr(instance, 'created_by'):
				instance.created_by = request.user
			instance.modified_by = request.user
			instance.save()
			form.save_m2m()
			return instance

	def save_formset(self, request, form, formset, change): 
		def set_user(instance):
			if not hasattr(instance, 'created_by'):
				instance.created_by = request.user
			instance.modified_by = request.user
			instance.save()

		if formset.model == User:
			instances = formset.save(commit=False)
			map(set_user, instances)
			formset.save_m2m()
			return instances
		else:
			return formset.save()


admin.site.register(StoryBundle)