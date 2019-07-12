from django.conf.urls import url
# from django.urls import path
from . import views

app_name= 'catalog'

urlpatterns = [
    url(r'^$', views.index,name = "index"),
    url(r'^books/$', views.BookListView.as_view(), name='books_list'),
    url(r'^book_detail/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book_detail'),
    url(r'^add/$', views.AddBook.as_view(), name='add_book'),

]
