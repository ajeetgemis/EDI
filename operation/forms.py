from django import forms
from .models import addmodel
from django.core import validators

class formaddmodel(forms.ModelForm):
    class Meta:
        model=addmodel
        fields=['asnnumber','gsdb','supplier','date','pknumber']
       # widgets={'asnnumber':forms.TextInput(attrs={'class':'form-control'}),
        #         'gsdb':forms.TextInput(attrs={'class':'form-control'}),
         ##      'date':forms.DateInput(attrs={'class':'form-control'}),
           #      'pknumber':forms.TextInput(attrs={'class':'form-control'}),
        
        #}