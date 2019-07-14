from datetime import datetime
from django.db import models
from django.urls import reverse
from djchoices import ChoiceItem, DjangoChoices

class Book(models.Model):
    """
    Model representing a book
    """
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.today())
    number_of_pages = models.IntegerField(default=0)
    is_first_edition = models.BooleanField(default=True)

    Engineering = 'ER'
    Medical = 'ME'
    Art = 'AR'
    Psychology = 'PS'
    Field_Category_CHOICES = [
        (Engineering, 'Engineering'),
        (Medical, 'Medical'),
        (Art, 'Art'),
        (Psychology, 'Psychology'),
    ]
    category = models.CharField(
        max_length=2,
        choices=Field_Category_CHOICES,
        default=Engineering,
    )


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


    def get_category_name(self):
        """
        Returns the url to access a particular book instance.
        """
        for choice in self.Field_Category_CHOICES:
            if choice[0] == self.category:
                return choice[1]