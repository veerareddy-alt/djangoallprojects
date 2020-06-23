from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hybjobsinfo(request):
    str="<h1>Wel Come to Hydarbed jobs</h1>"
    return HttpResponse(str)
def blorejobsinfo(request):
    str="<h1>Wel Come to Bangalore jobs</h1>"
    return HttpResponse(str)
def punejobsinfo(request):
    str="<h1>Wel Come to Pune jobs</h1>"
    return HttpResponse(str)
def chennaijobsinfo(request):
    str="<h1>Wel Come to Chennai jobs</h1>"
    return HttpResponse(str)
def mumbaijobsinfo(request):
    str="<h1>Wel Come to Mumbai jobs</h1>"
    return HttpResponse(str)
