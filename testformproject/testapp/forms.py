from django import forms
class TestForm(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    gender=forms.CharField()
    address=forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        inputname=self.cleaned_data['name']
        if len(inputname) <4:
            raise forms.ValidationError('the length of name should be greater then four')
        return inputname

    def clean_gender(self):
        inputgender=self.cleaned_data['gender']
        if (inputgender== 'm'or inputgender== 'M'):
            return inputgender
        elif(inputgender=='f' or inputgender=='F'):
            return inputgender
        else:
            raise forms.ValidationError('the gender should be M/F')
