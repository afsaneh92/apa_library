from django.shortcuts import render

from . import models

def index(request):
    """
    View function for home page of site.
    """
    # Generate some of the main objects
    title=models.Book.objects.all().count()
    pub_date=models.Book.objects.all().count()
    number_of_pages=models.Book.objects.all().count()
    is_first_edition=models.Book.objects.all().count()

    # Render the HTML template index.html
    return render(
        request,
        'catalog/index.html',
        context={'books_title':title,'pub_date':pub_date,
                 'number_of_pages' : number_of_pages,
                 'is_first_edition':is_first_edition},
    )
