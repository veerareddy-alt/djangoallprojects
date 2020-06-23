from django.shortcuts import render,redirect
from testapp.models import Student
from testapp.forms import StudentForm

# Create your views here.
def homeview(request):
    stud=Student.objects.all()
    return render (request,'testapp/home.html',{'stud':stud})

def createview(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'testapp/create.html',{'form':form})

def deleteview(request,id):
    s=Student.objects.get(id=id)
    s.delete()
    return redirect('/')

def updateview(request,id):
    s=Student.objects.get(id=id)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'testapp/update.html',{'s':s})
