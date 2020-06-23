from django.shortcuts import render
from . import forms

# Create your views here.
def feedbackview(request):
    fb=forms.FeedbackForm()
    if request.method=='POST':
        fb=forms.FeedbackForm(request.POST)
        if fb.is_valid():
            print("validation sucessfully")
            print("student name",fb.cleaned_data['name'])
            print("student rollno",fb.cleaned_data['rollno'])
            print("student email",fb.cleaned_data['email'])
            print("student feedback",fb.cleaned_data['feedback'])
            return render (request,'testapp/thanku.html',{'name':fb.cleaned_data['name']})
    return render(request,'testapp/feedback.html',{'fb':fb})
