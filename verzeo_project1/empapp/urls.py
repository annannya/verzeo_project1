from django.urls import re_path
from empapp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                
            re_path('all_employee', views.all_employee, name='all_employee'),
            re_path('add_employee', views.add_employee, name='add_employee'),
            re_path('remove_employee', views.remove_employee, name='remove_employee'),
            re_path('filter_employee', views.filter_employee, name='filter_employee'),
            re_path('', views.index, name='index'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)