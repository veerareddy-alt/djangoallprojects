from django.shortcuts import render
from django.views.generic import ListView,DetailView
from testapp.models import Book

# Create your views here.
class BookListView(ListView):
    model=Book
    #default template address=book_list.html
    #default context=book_list
    template_name='testapp/book.html'
    context_object_name='list_of_book'

class BookDetailView(DetailView):
    model=Book
    #default template name=book_detail.AuthenticationMiddleware
    #default context=book or object
