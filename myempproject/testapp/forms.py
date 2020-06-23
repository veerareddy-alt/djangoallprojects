from django import forms
from testapp.models import EmpModel
class EmpForm(forms.ModelForm):
    class Meta:
        model=EmpModel
        fields='__all__'
