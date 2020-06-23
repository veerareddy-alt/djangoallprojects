from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q

# Create your views here.
def employeelist(request):
    # e=Employee.objects.create(eno=6666,ename='veeru',esal=30550,eaddr='blore')
    # e=Employee(eno=6663,ename='veera',esal=30650,eaddr='glb')
    # e1=Employee(eno=6669,ename='veerareddypatil',esal=20650,eaddr='glb')
    # e2=Employee(eno=6664,ename='veerareddy',esal=23650,eaddr='nasik')
    # e3=Employee(eno=6668,ename='veerapatil',esal=30650,eaddr='glb')
     # -*- coding: utf-8 -*-
    # Employee.objects.bulk_create([e1,e2,e3])

    # e.save()

    employees=Employee.objects.all()
    # qs=Employee.objects.get(id=40)
    # employees=Employee.objects.filter(ename__contains='Da')
    # employees=Employee.objects.filter(id__in=[35,36,37,38,39])
    # employees=Employee.objects.filter(ename__startswith='D')
    # employees=Employee.objects.filter(ename__endswith='s')
    # employees=Employee.objects.filter(esal__range=(22000,25000))
    # employees=Employee.objects.filter(esal__range=(22000,25000)) |Employee.objects.filter(ename__startswith='D')
    # employees=(Employee.objects.filter(esal__range=(22000,25000))) &(Employee.objects.filter(ename__startswith='D'))
    # employees=(Employee.objects.filter(esal__range=(22000,25000))) |(Employee.objects.filter(ename__startswith='J'))
    # employees=Employee.objects.exclude(esal__range=(22000,25000))
    # employees=Employee.objects.filter(~Q(esal__range=(20000,25000)))




    # mydict=employees
    return render(request,'testapp/home.html',{'employees':employees})
