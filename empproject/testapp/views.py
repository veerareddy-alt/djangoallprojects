from django.shortcuts import render
from testapp.models import Employee

# Create your views here.
def homepage(request):
    return render(request,'testapp/homepage.html')
def empinfo(request):
    emp_list=Employee.objects.all()
    mydict={'emp_list':emp_list}
    return render(request,'testapp/emp.html',context=mydict)
