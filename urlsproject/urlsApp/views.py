from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hybjobinfo(request):
    s="<h1>Welcome to Hydarabed jobs"
    return HttpResponse(s)

def punejobinfo(request):
    s="<h1>Welcome to pune jobs"
    return HttpResponse(s)

def chennaijobinfo(request):
    s="<h1>Welcome to chennai jobs"
    return HttpResponse(s)

def mumbaijobinfo(request):
    s="<h1>Welcome to mumbai jobs"
    return HttpResponse(s)
