from django import forms
class AddIteamForm(forms.Form):
    name=forms.CharField()
    quantity=forms.IntegerField()
