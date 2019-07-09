from datetime import datetime
from django.db import models

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

