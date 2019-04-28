from django.urls import path
from .views import *

urlpatterns = [
    path('create/', notice_create, name='notice_create'),

]