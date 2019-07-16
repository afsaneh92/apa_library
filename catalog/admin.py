from django.contrib import admin
from .models import Book

from django.contrib import admin
from jalali_date.admin import (
    ModelAdminJalaliMixin,
    StackedInlineJalaliMixin,
    TabularInlineJalaliMixin,
)

# Register your models here.


@admin.register(Book)
class BookModelAmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    pass