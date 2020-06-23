from django.shortcuts import render
import datetime

# Create your views here.
def infofun(request):
    date=datetime.datetime.now()
    name="veerareddy"
    mydict={'date_msg':date,'name':name}
    return render(request,'testapp/msg.html',context=mydict)
