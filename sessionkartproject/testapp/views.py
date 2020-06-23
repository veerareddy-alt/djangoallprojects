from django.shortcuts import render
from testapp.forms import AddIteamForm

# Create your views here.
def additeamview(request):
    form=AddIteamForm()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
    return render (request,'testapp/iteam.html',{'form':form})

def thankuview(request):
    return render(request,'testapp/thanku.html')
