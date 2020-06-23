from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome(request):
    s="<h1>Hello welcome to django</h1>"+"<h1> GOOD WORK !!!!!!!!!</h1>"
    return HttpResponse(s)
