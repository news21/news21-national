from django import forms
from photos.models import Photo, Image
from multimedia.forms import FileWidget

class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ('pub_date','site','slug','created_by', 'modified_by', 'created','modified','image')

class ImageForm(forms.ModelForm):

    image = forms.FileField( widget=FileWidget, )

    class Meta:
        model = Image
        fields = ('image',)
