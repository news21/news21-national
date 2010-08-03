from django import forms
from news21national.photos.models import Photo, Image

from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Row, HTML

class PhotoForm(forms.ModelForm):
	helper = FormHelper()

	layout = Layout(
		Fieldset('',
			'title','date_taken','summary','slug',
			css_class='inlineLabels',),
			
	)

	helper.add_layout(layout)
	
	class Meta:
		model = Photo
		exclude = ('story','status','attribution','license','pub_date','is_active','authors','image','created_at','created_by','updated_at','updated_by','tags','stage')

class ImageForm(forms.ModelForm):

	image = forms.ImageField(  )

	class Meta:
		model = Image
		fields = ('image',)