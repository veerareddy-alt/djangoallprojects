from django.shortcuts import render
from testapp import forms
from testapp.models import Movie

# Create your views here.
def homeview(request):
    return render(request,'testapp/moviehome.html')

def addmovieview(request):
    mf=forms.MovieForm()

    if request.method=='POST':
        mf=forms.MovieForm(request.POST)
        if mf.is_valid():
            mf.save(commit=True)
            return homeview(request)
    return render(request,'testapp/addmovie.html',{'mf':mf})

def listmovieview(request):
    movie_list=Movie.objects.all()
    return render(request,'testapp/listmovie.html',{'movie_list':movie_list})
