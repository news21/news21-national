from django.contrib import admin
from news21national.editorsdesk.models import EditorsDesk
from news21national.core.models import Profile
from django import forms

class EditorsDeskForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(EditorsDeskForm, self).__init__(*args, **kwargs)
		profiles = Profile.objects.all();
		s = self.fields['editors'].widget
		choices = []
		for choice in profiles:
			choices.append((choice.user.id, '('+choice.school+') '+choice.first_name+ ' '+choice.last_name+' ( '+str(choice.user.email)+' )' ))
		s.choices = sorted(choices, key=lambda c: c[1])

class EditorsDeskAdmin(admin.ModelAdmin):
	form = EditorsDeskForm

admin.site.register(EditorsDesk,EditorsDeskAdmin)