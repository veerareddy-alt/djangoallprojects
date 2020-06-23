from django.shortcuts import render
from testapp import forms
from testapp.models import HomeModel
from testapp.forms import HomeForm


# Create your views here.
def homeview(request):
    form=HomeForm()
    return render(request,'testapp/homepage.html',{'form':form})
