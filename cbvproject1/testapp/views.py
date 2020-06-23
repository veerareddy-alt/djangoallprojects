from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse


# Create your views here.
class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1>welcome to class based view</h1>')

class HelloWorldTemplateView(TemplateView):
    template_name='testapp/result.html'

class HelloWorldContextview(TemplateView):
    template_name='testapp/stu.html'
    def get_context_date(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='veeru'
        context['subject']='python'
        context[marks]=90
        return context
