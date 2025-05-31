# main_app/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def vehicle_index(req):
    vehicles = Vehicle.objects.all()
    return render(req, 'vehicles/index.html', {'vehicles': vehicles})

def vehicle_detail(req, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    return render(req, 'vehicles/detail.html', {'vehicle': vehicle})

class VehicleCreate(CreateView):
    model = Vehicle
    fields = '__all__'

class VehicleUpdate(UpdateView):
    model = Vehicle
    fields = '__all__'

class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = '/vehicles/'