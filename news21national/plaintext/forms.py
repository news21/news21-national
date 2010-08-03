from django import forms
from news21national.plaintext.models import PlainText
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import Select
from news21national.multimedia.constants import STAGE_CHOICES, STAGE_DEFAULT, STATUS_DEFAULT, STATUS_CHOICES
from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Row, HTML


class PlainTextForm(forms.ModelForm):
	helper = FormHelper()

	layout = Layout(
		Fieldset('',
			'title','summary','content','slug',
			css_class='inlineLabels',),
	)

	helper.add_layout(layout)

	class Meta:
		model = PlainText
		exclude = ('story','status','attribution','is_active','license','pub_date','authors','created_at','created_by','updated_at','updated_by','tags','stage')

