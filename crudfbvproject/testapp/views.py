from django.shortcuts import render,redirect
from testapp.models import Employee
from testapp.forms import EmployeeForm

# Create your views here.
def retriveview(request):
    employees=Employee.objects.all()
    return render(request,'testapp/index.html',{'employees':employees})

def createview(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    return render(request,'testapp/create.html',{'form':form})

def deleteview(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')

def updateview(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render (request,'testapp/update.html',{'employee':employee})
