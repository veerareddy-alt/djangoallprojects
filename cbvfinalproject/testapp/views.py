from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from testapp.models import Beer

# Create your views here.
class BeerListView(ListView):
    model=Beer

class BeerDetailView(DetailView):
    model=Beer

class BeerCreateView(CreateView):
    model=Beer
    fields='__all__'

class BeerUpadateView(UpdateView):
    model=Beer
    fields=('taste','color','price')
