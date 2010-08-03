from django import forms
from news21national.videos.models import Video

from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Row, HTML

class VideoForm(forms.ModelForm):
	helper = FormHelper()

	layout = Layout(
		Fieldset('',
			'title','video','hq_file','date_taken','duration','summary','slug',
			css_class='inlineLabels',),
			
	)

	helper.add_layout(layout)

	class Meta:
		model = Video
		exclude = ('story','status','attribution','license','pub_date','is_active','authors','created_at','created_by','updated_at','updated_by','tags','stage')
