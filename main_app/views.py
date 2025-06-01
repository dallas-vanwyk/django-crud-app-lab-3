# main_app/views.py

from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Vehicle
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import MaintenanceForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

def about(req):
    return render(req, 'about.html')

@login_required
def vehicle_index(req):
    vehicles = Vehicle.objects.filter(user=req.user)
    return render(req, 'vehicles/index.html', {'vehicles': vehicles})

@login_required
def vehicle_detail(req, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    maintenance_form = MaintenanceForm()
    return render(req, 'vehicles/detail.html', {
        'vehicle': vehicle,
        'maintenance_form': maintenance_form,
    })

class VehicleCreate(LoginRequiredMixin, CreateView):
    model = Vehicle
    fields = ['modelyear', 'make', 'model']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class VehicleUpdate(LoginRequiredMixin, UpdateView):
    model = Vehicle
    fields = ['modelyear', 'make', 'model']

class VehicleDelete(LoginRequiredMixin, DeleteView):
    model = Vehicle
    success_url = '/vehicles/'

@login_required
def add_maintenance(req, vehicle_id):
    form = MaintenanceForm(req.POST)
    if form.is_valid():
        new_maintenance = form.save(commit=False)
        new_maintenance.vehicle_id = vehicle_id
        new_maintenance.save()
    return redirect('vehicle-detail', vehicle_id=vehicle_id)

def signup(req):
    error_message = ''
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('vehicle-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(req, 'signup.html', context)