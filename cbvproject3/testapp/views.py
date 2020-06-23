from django.shortcuts import render
from testapp.models import Company
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class CompanyListView(ListView):
    model=Company

class CompanyDetailView(DetailView):
    model=Company

class CompanyCreateView(CreateView):
    model=Company
    fields=('name','location','ceo')
    #default template name=company_form.html

class CompanyUpdateView(UpdateView):
        model=Company
        fields=('name','location','ceo')
    #default template name=company_form.html

class CompanyDeleteView(DeleteView):
    model=Company
    success_url=reverse_lazy('companies')
