from django.shortcuts import render
from . import forms

# Create your views here.
def testformviews(request):
    tf=forms.TestForm()
    if request.method=='POST':
        tf=forms.TestForm(request.POST)
        if tf.is_valid():
            print("validation id done")
            print("Name :",tf.cleaned_data['name'])
            print("Age :",tf.cleaned_data['age'])
            print("Gender :",tf.cleaned_data['gender'])
            print("Address :",tf.cleaned_data['address'])
            return render(request,'testapp/thanku.html',{'name':tf.cleaned_data['name']})
    return render(request,'testapp/tstform.html',{'tf':tf})
