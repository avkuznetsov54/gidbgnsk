from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from .views import jkobjects_index, JkobjectsDetailView
from .views import building_search


urlpatterns = [
    path('', jkobjects_index, name='jkobjects_index_url'),
    path('detail/<int:pk>/', JkobjectsDetailView.as_view(), name='detail'),

    # ajax
    path('search/', building_search, name='building_search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)