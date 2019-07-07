from django import forms
from .models import Tip

class TipForm(forms.ModelForm):
    class Meta:
        model=Tip
        fields=['title','body','file']

    def __init__(self,*args,**kwargs):
        super(TipForm,self).__init__(*args,**kwargs)
        self.fields['file'].required=False