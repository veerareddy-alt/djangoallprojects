from django.shortcuts import render
from . import forms
# Create your views here.
def myformview(request):
    if request.method=='GET':
        mf=forms.MyFormRegister()
        return render(request,'testapp/myform.html',{'mf':mf})
    if request.method=='POST':
            mf=forms.MyFormRegister(request.POST)
            if mf.is_valid():
                print("validation done")
                print("Name",mf.cleaned_data['name'])
                print("Age",mf.cleaned_data['age'])
                print("Gender",mf.cleaned_data['gender'])
                print("Email",mf.cleaned_data['email'])
                print("Password",mf.cleaned_data['password'])
                print("Password_again",mf.cleaned_data['password_again'])
                print("Address",mf.cleaned_data['address'])
                return render(request,'testapp/thanku.html',{'name':mf.cleaned_data['name']})
    return render(request,'testapp/myform.html',{'mf':mf})
