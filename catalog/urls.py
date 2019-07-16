from django.conf.urls import url
# from django.urls import path
from . import views

app_name= 'catalog'

urlpatterns = [
    url(r'^$', views.index,name = "index"),
    url(r'^books/$', views.BookListView.as_view(), name='books_list'),
    url(r'^book_detail/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book_detail'),
    url(r'^book/create/$', views.BookCreate.as_view(), name='add_book'),
    url(r'^book/(?P<pk>[-\w]+)/edit/$', views.BookEdit.as_view(), name='edit-book'),
    url(r'^book/(?P<pk>[-\w]+)/delete/$', views.BookDelete.as_view(), name='delete-book'),

]
