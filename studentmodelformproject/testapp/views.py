from django.shortcuts import render
from testapp import forms


# Create your views here.
def studentview(request):
    sf=forms.StudentForm()
    if request.method=='POST':
        sf=forms.StudentForm(request.POST)
        if sf.is_valid():
            sf.save(commit=True)
            print("Data Insterted Successfully")
    return render(request,'testapp/stureg.html',{'sf':sf})
