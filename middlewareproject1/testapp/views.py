from django.shortcuts import render
from django.http import HttpResponse
def middlewareview(request):
    print('this statement is executed in view function')
    # print(9/0)
    return HttpResponse("<h1>MIDDLEWARE TESTING</h1>")


# Create your views here.
