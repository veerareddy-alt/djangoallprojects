from django import forms
from testapp.models import Filtermodel

class FilterForm(forms.ModelForm):
    class Meta:
        model=Filtermodel
        fields='__all__'
