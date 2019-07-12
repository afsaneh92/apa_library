from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, DeleteView, UpdateView

from catalog.models import Book
from . import models

def index(request):
    """
    View function for home page of site.
    """
    # Generate some of the main objects
    number=models.Book.objects.all().count()
    # pub_date=models.Book.objects.all().count()
    # number_of_pages=models.Book.objects.all().count()
    # is_first_edition=models.Book.objects.all().count()

    # Render the HTML template index.html
    return render(
        request,
        'catalog/index.html',
        context={'books_num':number},
    )
# return render(
#         request,
#         'catalog/index.html',
#         context={'books_num':number,'pub_date':pub_date,
#                  'number_of_pages' : number_of_pages,
#                  'is_first_edition':is_first_edition},
class BookListView(generic.ListView):
    model = models.Book
    template_name = 'catalog/book_list.html'

class AddBook(generic.ListView):
    model = models.Book
    template_name = 'catalog/add_book.html'

class BookDetailView(generic.DetailView):
    model = models.Book
    template_name='catalog/book_detail.html'

class BookCreate(generic.CreateView):
    model = models.Book
    fields = "__all__"
    # initial =
    template_name = 'catalog/add_book.html'

class BookEdit(generic.UpdateView):
    model = models.Book
    fields = "__all__"
    template_name = 'catalog/add_book.html'

class BookDelete(generic.DeleteView):
    model = models.Book
    template_name = 'catalog/delete_book.html'
    success_url = reverse_lazy('catalog:books_list')