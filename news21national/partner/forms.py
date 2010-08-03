from django import forms
from news21national.partner.models import Partner

from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Row, HTML

class PartnerForm(forms.ModelForm):
	helper = FormHelper()

	layout = Layout(
		Fieldset('',
			'name','site_url','phone','email',
			css_class='inlineLabels',),
	)
	
	helper.add_layout(layout)
	
	class Meta:
		model = Partner
		exclude = ('members','created_by','created_at','updated_by','updated_at')