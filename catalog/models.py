from datetime import datetime
from django.db import models
from django.urls import reverse

class Book(models.Model):
    """
    Model representing a book
    """
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.today())
    number_of_pages = models.IntegerField(default=0)
    is_first_edition = models.BooleanField(default=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('catalog:book_detail', args=[str(self.id)])

def add_book():
    pass