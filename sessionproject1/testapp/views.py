from django.shortcuts import render

# Create your views here.
def countview(request):
    count=request.session.get('count',0)
    newcount=count+1
    request.session['count']=newcount
    request.session.set_expiry(180)
    return render(request,'testapp/count.html',{'count':newcount})
