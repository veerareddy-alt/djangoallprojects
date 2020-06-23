from django.shortcuts import render
from testapp import forms
from testapp.models import Filtermodel

# Create your views here.
def filterview(request):
    ff=forms.FilterForm()

    if request.method =='POST':
        ff=forms.FilterForm(request.POST)
        if ff.is_valid():
            ff.save(commit=True)
            return render (request,'testapp/homefilter.html',{'ff':ff})
    return render (request,'testapp/homefilter.html',{'ff':ff})

def upperview(request):
    filter_list=Filtermodel.objects.all()
    return render(request,'testapp/upperfilter.html',{'filter_list':filter_list})

def lowerview(request):
    filter_list=Filtermodel.objects.all()
    return render(request,'testapp/lowerfilter.html',{'filter_list':filter_list})

def titleview(request):
    filter_list=Filtermodel.objects.all()
    return render(request,'testapp/titlefilter.html',{'filter_list':filter_list})
