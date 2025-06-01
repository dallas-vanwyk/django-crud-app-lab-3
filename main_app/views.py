# main_app/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vehicle
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import MaintenanceForm

def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def vehicle_index(req):
    vehicles = Vehicle.objects.all()
    return render(req, 'vehicles/index.html', {'vehicles': vehicles})

def vehicle_detail(req, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    maintenance_form = MaintenanceForm()
    return render(req, 'vehicles/detail.html', {
        'vehicle': vehicle,
        'maintenance_form': maintenance_form,
    })

class VehicleCreate(CreateView):
    model = Vehicle
    fields = '__all__'

class VehicleUpdate(UpdateView):
    model = Vehicle
    fields = '__all__'

class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = '/vehicles/'

def add_maintenance(req, vehicle_id):
    form = MaintenanceForm(req.POST)
    if form.is_valid():
        new_maintenance = form.save(commit=False)
        new_maintenance.vehicle_id = vehicle_id
        new_maintenance.save()
    return redirect('vehicle-detail', vehicle_id=vehicle_id)