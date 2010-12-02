from django import forms
from news21national.links.models import Link

from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Row, HTML

class LinkForm(forms.ModelForm):
	
	helper = FormHelper()

	layout = Layout(
		Fieldset('',
			'title','url','summary','slug',
			css_class='inlineLabels',),
	)

	helper.add_layout(layout)

	class Meta:
		model = Embed
		exclude = ('story','status','attribution','license','is_active','pub_date','authors','created_at','created_by','updated_at','updated_by','tags','stage')