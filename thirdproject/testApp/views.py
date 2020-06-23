from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hybjobsinfo(request):
    msg1="<h1>Hyderabad job information!!!!!!</h1>"
    return HttpResponse(msg1)
def blorejobsinfo(request):
    msg1="<h1>Banglore job information!!!!!!</h1>"
    return HttpResponse(msg1)
def punejobsinfo(request):
    msg1="<h1>Pune job information!!!!!!</h1>"
    return HttpResponse(msg1)
def chennaijobsinfo(request):
    msg1="<h1>Chennai job information!!!!!!</h1>"
    return HttpResponse(msg1)
def mumbaijobsinfo(request):
    msg1="<h1>Mumbai job information!!!!!!</h1>"
    return HttpResponse(msg1)
