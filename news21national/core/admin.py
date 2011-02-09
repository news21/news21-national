from django.contrib import admin
from news21national.core.models import Profile
from django.http import HttpResponse

def export_to_csv(model_admin, request, queryset):
	li_return = ""
	li_columns = []
	for model_object in queryset.all():
		if not li_columns:
			for a_field in model_object._meta.fields:
				li_columns.append(a_field.name)
				li_return += ",\"%s\"" % a_field.name
			li_return = li_return[1:] + "\n"
		s_row = ""
		for col_name in li_columns:
			s_row += ",\"%s\"" % unicode(getattr(model_object, col_name))
		s_row = s_row[1:] + "\n"
		li_return += s_row

	response = HttpResponse(mimetype="text/csv")
	response['content-Disposition'] = 'attachment; filename=csv_export.csv'
	response.write(li_return)
	return response

export_to_csv.short_description = "Export selected as CSV"

admin.site.add_action(export_to_csv, "export_to_csv")


def export_to_tab(model_admin, request, queryset):
	li_return = ""
	li_columns = []
	for model_object in queryset.all():
		if not li_columns:
			for a_field in model_object._meta.fields:
				li_columns.append(a_field.name)
				li_return += "\t\"%s\"" % a_field.name
			li_return = li_return[1:] + "\n"
		s_row = ""
		for col_name in li_columns:
			s_row += "\t\"%s\"" % unicode(getattr(model_object, col_name))
		s_row = s_row[1:] + "\n"
		li_return += s_row

	response = HttpResponse(mimetype="text/txt")
	response['content-Disposition'] = 'attachment; filename=tab_export.txt'
	response.write(li_return)
	return response

export_to_tab.short_description = "Export selected as TAB Delim"

admin.site.add_action(export_to_tab, "export_to_tab")

class ProfileAdmin(admin.ModelAdmin):
	list_display = ['first_name','last_name','is_active',]
	list_filter = ['is_active','school']
	ordering = ['last_name',]
	search_fields = ['first_name','last_name',]

admin.site.register(Profile, ProfileAdmin)

