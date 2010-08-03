from django import forms
from news21national.swfs.models import Swf

class SwfForm(forms.ModelForm):
    
    class Meta:
        model = Swf
        exclude = ('story','status','attribution','license','pub_date','authors','created_at','created_by','updated_at','updated_by','tags')

    def __init__(self, *args, **kwargs):
        super(SwfForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['title','zip_file','flash_compat','width','height','summary','slug']
