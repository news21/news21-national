from django import forms
from news21national.audio.models import Audio

from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Row, HTML

class AudioForm(forms.ModelForm):
	helper = FormHelper()

	layout = Layout(
		Fieldset('',
			'title','audio','summary','slug',
			css_class='inlineLabels',),
			
	)

	helper.add_layout(layout)
	
	class Meta:
		model = Audio
		exclude = ('story','status','attribution','license','pub_date','authors','created_at','created_by','updated_at','updated_by','tags','stage')