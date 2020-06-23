from django.shortcuts import render

# Create your views here.
def nameview(request):
    return render(request,'testapp/name.html')

def ageview(request):
    name=request.GET['name']
    response=render(request,'testapp/age.html',{'name':name})
    response.set_cookie('name',name)
    return response

def addressview(request):
    age=request.GET['age']
    name=request.COOKIES.get('name')

    response=render(request,'testapp/address.html',{'name':name})
    response.set_cookie('age',age)
    return response

def companyview(request):
    address=request.GET['address']
    name=request.COOKIES.get('name')
    response=render(request,'testapp/company.html',{'name':name})
    response.set_cookie('address',address)
    return response

def detailsview(request):
    company=request.GET['company']
    name=request.COOKIES.get('name')
    age=request.COOKIES.get('age')
    address=request.COOKIES.get('address')
    
    response=render(request,'testapp/details.html',{'name':name,'age':age,'address':address,'company':company})
    return response
