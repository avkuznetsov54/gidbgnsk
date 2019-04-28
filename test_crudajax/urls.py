from django.urls import path
from .views import *

urlpatterns = [
    path('save/', test1, name="test1"),
    path('books/', book_list, name='book_list'),
    path('books/create/', book_create, name='book_create'),
    path('books/<id>/update/', book_update, name='book_update'),
    path('books/<id>/delete/', book_delete, name='book_delete'),
]