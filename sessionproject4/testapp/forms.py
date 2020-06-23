from django import forms
from testapp.models import HomeModel
class HomeForm(forms.ModelForm):
    class Meta:
        model:HomeModel
        fields='__all__'
