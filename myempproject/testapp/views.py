from django.shortcuts import render
from testapp.forms import EmpForm
from testapp.models import EmpModel

# Create your views here.
def empformview(request):
    form=EmpForm()
    if request.method=='POST':
        form=EmpForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
    return render(request,'testapp/emplogin.html',{'form':form})

def displayview(request):
    emp_list=EmpModel.objects.all()
    return render(request,'testapp/empdetails.html',{'emp_list':emp_list})
