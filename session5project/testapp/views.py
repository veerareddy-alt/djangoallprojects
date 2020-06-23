from django.shortcuts import render

from testapp.forms import ItemForm
# Create your views here.
def itemformview(request):
    form=ItemForm()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
    return render (request,'testapp/additem.html',{'form':form})

def displayview(request):
    return render(request,'testapp/displayitem.html')
