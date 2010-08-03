from django import forms

from django.forms.widgets import Select, Textarea
from news21national.editorsdesk.constants import STAGE_CHOICES, STAGE_DEFAULT, STATUS_DEFAULT, STATUS_CHOICES
from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Row, HTML

class EditorsCommentForm(forms.Form):
	stage = forms.CharField(label="Stage", required=False, widget=Select(choices=(STAGE_CHOICES)))
	status = forms.CharField(label="Status", required=True, widget=Select(choices=(STATUS_CHOICES)))
	comment = forms.CharField(label="Comment", required=False, widget=Textarea())
	
	helper = FormHelper()

	layout = Layout(
		Fieldset('',
			'stage','status','comment',
			css_class='inlineLabels',),
	)
	
	submit = Submit('save','Comment')
	helper.add_input(submit)

	helper.add_layout(layout)