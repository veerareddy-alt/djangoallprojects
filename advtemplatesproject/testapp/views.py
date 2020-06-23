from django.shortcuts import render

# Create your views here.
def homeview(request):
    return render (request,'testapp/newshome.html')

def moviesview(request):
    return render (request,'testapp/movies.html')

def sportsview(request):
    return render (request,'testapp/sports.html')

def generalview(request):
    return render (request,'testapp/general.html')
