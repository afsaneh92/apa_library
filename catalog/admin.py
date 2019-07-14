from django.contrib import admin
from .models import Book

from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin

admin.site.register(Book)
#
# class MyInlines1(TabularInlineJalaliMixin, admin.TabularInline):
#     model = Book
#
#
# class MyInlines2(StackedInlineJalaliMixin, admin.StackedInline):
#     model = Book

#
# @admin.register(Book)
# class FirstModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
#     # inlines = (MyInlines1, MyInlines2,)
#     model = Book
#     raw_id_fields = ('some_fields',)
#     readonly_fields = ('some_fields', 'date_field',)
#     # you can override formfield, for example:
#     # formfield_overrides = {
#     #     JSONField: {'widget': JSONEditor},
#     # }