"""gidbgnsk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from .views import home
from .views import login_view, logout_view

from contract_orgs.views import contract_orgs_index

# from gen_notices.views import fields_notice
# from gen_notices.views import loadBlockB
# from gen_notices.views import FieldsNoticeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home, name='home'),

    path('buildings/', include(('jk_objects.urls', 'jk_objects')), name='buildings'),

    path('contract-orgs/', contract_orgs_index, name='contract_orgs'),

    path('test-sendmail/', include(('test_sendmail.urls', 'test_sendmail'))),

    # path('form/', FieldsNoticeView.as_view(), name='fields_notice'),

    # ajax
    path('notice/', include(('gen_notices.urls', 'gen_notice'))),

    # ajax test
    path('test-crudajax/', include(('test_crudajax.urls', 'test_crudajax'))),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
