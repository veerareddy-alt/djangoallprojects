from django.shortcuts import render
from . import form

# Create your views here.
def studentregisterviews(request):
    f=form.StudentRegister()
    return render(request,'testapp/register.html',{'f':f})
