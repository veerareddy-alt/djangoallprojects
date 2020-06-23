from django.shortcuts import render
from testapp.forms import NameForm,AgeForm,GfForm

# Create your views here.
def nameview(request):
    form=NameForm()
    return render(request,'testapp/name.html',{'form':form})

def ageview(request):
    name=request.GET['name']
    request.session['name']=name
    form=AgeForm()
    return render(request,'testapp/age.html',{'form':form,'name':name})

def gfview(request):
    age=request.GET['age']
    name=request.session.get('name')
    request.session['age']=age
    form=GfForm()
    return render(request,'testapp/gf.html',{'form':form,'name':name,'age':age})

def thankuview(request):
    # name=request.session.get('name')
    # age=request.session.get('age')
    gf=request.GET['gf']
    request.session['gf']=gf
    # return render(request,'testapp/thanku.html',{'name':name,'age':age,'gf':gf})
    return render(request,'testapp/thanku.html')
