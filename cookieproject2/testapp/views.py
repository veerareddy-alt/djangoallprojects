from django.shortcuts import render

# Create your views here.
def nameview(request):
    return render (request,'testapp/name.html')

def ageview(request):
    name=request.GET['name']
    response= render(request,'testapp/age.html')
    response.set_cookie('name',name)
    return response

def gfview(request):
    age=request.GET['age']
    response=render(request,'testapp/gf.html')
    response.set_cookie('age',age)
    return response

def thankuview(request):
    gf=request.GET['gf']
    name=request.COOKIES.get('name')
    age=request.COOKIES.get('age')

    response=render(request,'testapp/thanku.html',{'name':name,'age':age,'gf':gf})
    return response
