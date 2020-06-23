from django.shortcuts import render

# Create your views here.
def nameveiw(request):
    return render(request,'testapp/name.html')

def ageview(request):
    name=request.GET['name']
    request.session['name']=name
    return render(request,'testapp/age.html',{'name':name})

def gfview(request):
    age=request.GET['age']
    name=request.session.get('name')
    request.session['age']=age
    return render(request,'testapp/gf.html',{'age':age,'name':name})

def thankuview(request):
    gf=request.GET['gf']
    request.session['gf']=gf
    name=request.session.get('name')
    age=request.session.get('age')
    return render(request,'testapp/thanku.html',{'gf':gf,'name':name,'age':age})
