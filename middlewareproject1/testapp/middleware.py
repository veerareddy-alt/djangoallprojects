class ExcutionMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print("this statement is executed in preprocessing")
        response=self.get_response(request)
        print("this statement is executed after processing")
        return response

from django.http import HttpResponse
class AppMaintanceMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        s="<h1>the site is under maintance so plz try after sometime<h1>"
        return HttpResponse(s)

class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_exception(self,request,exception):
        s1="<h1>There is some techinacal issue</h1><hr> "
        s2="<h1>Raised Exception is :{}</h1>".format(exception.__class__.__name__)
        s3="<h1>Description od Exception is :{}</h1>".format(exception)
        return HttpResponse(s1+s2+s3)

class FirstMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("this is firstmiddleware per processing")
        response=self.get_response(request)
        print("this is FirstMiddleware after post processing")
        return response


class SecondMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("this is secondmiddleware per processing")
        response=self.get_response(request)
        print("this is secondMiddleware after post processing")
        return response


class ThirdMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("this is thirdmiddleware per processing")
        response=self.get_response(request)
        print("this is thirdMiddleware after post processing")
        return response
