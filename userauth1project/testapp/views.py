from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect


# Create your views here.
def homeview(request):
    return render(request,'testapp/home.html')

@login_required
def javaexamview(request):
    return render (request,'testapp/javaexam.html')
@login_required
def pythonexamview(request):
    return render (request,'testapp/pythonexam.html')
@login_required
def apititudeexamview(request):
    return render (request,'testapp/apititudexam.html')

def logoutview(request):
    return render(request,'testapp/logout.html')

def signupformview(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')

    return render(request,'testapp/signup.html',{'form':form})
