# main_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vehicles/', views.vehicle_index, name='vehicle-index'),
    path('vehicles/<int:vehicle_id>', views.vehicle_detail, name='vehicle-detail'),
    path('cats/create/', views.VehicleCreate.as_view(), name='vehicle-create'),
]
