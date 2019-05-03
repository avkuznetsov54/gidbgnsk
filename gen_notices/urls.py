from django.urls import path
from django.conf.urls.static import static

from .views import *

urlpatterns = [

    # ajax
    path('create/', notice_create, name='notice_create'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)