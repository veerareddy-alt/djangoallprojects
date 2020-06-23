from django.shortcuts import render
from testapp.models import StudentInfo
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class StudentInfoListView(ListView):
    model=StudentInfo

class StudentInfoDetailView(DetailView):
    model=StudentInfo

class StudentInfoCreateView(CreateView):
    model=StudentInfo
    fields=('name','rollno','addr')

class StudentInfoUpdateView(UpdateView):
    model=StudentInfo
    fields=('name','rollno')

class StudentInfoDeleteView(DeleteView):
    model=StudentInfo
    success_url=reverse_lazy('stud')
