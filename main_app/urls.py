# main_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vehicles/', views.vehicle_index, name='vehicle-index'),
    path('vehicles/<int:vehicle_id>', views.vehicle_detail, name='vehicle-detail'),
    path('vehicles/create/', views.VehicleCreate.as_view(), name='vehicle-create'),
    path('vehicles/<int:pk>/update/', views.VehicleUpdate.as_view(), name='vehicle-update'),
    path('vehicles/<int:pk>/delete/', views.VehicleDelete.as_view(), name='vehicle-delete'),
]
