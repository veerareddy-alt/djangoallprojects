from django import forms
from django.core import validators

def gmailverification(value):
    if value[len(value)-9:]!='gmail.com':
        raise forms.ValidationError("mail id should be gmail.com")
class MyFormRegister(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    gender=forms.CharField(validators=[validators.MaxLengthValidator(1),validators.MinLengthValidator(1)])
    email=forms.EmailField(validators=[gmailverification])
    password=forms.CharField(widget=forms.PasswordInput)
    password_again=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40)])

    def clean(self):
        cleaned_data=super().clean()
        inputname=cleaned_data['name']
        if (len(inputname)<5) or  (inputname.isalpha()!=True):
            raise forms.ValidationError('name field should be character only and minimum of 5 character')
        inputage=cleaned_data['age']
        if inputage <18 or inputage>50:
            raise forms.ValidationError("Age should be between 18-50")
        inputpwd=cleaned_data['password']
        inputpwda=cleaned_data['password_again']
        if len(inputpwd) <8:
            raise forms.ValidationError("password should be minimum of 8 length")
        if inputpwd != inputpwda:
            raise forms.ValidationError("password does not match")
        
