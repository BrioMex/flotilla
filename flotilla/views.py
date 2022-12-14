from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Vehicle
from .forms import VehicleForm


# Create your views here.
def home(request):
    return render(request, 'vehicles/home.html', {}) #request always, which template are we going to, what are we sending there

def all_vehicles(request):
    vehicles_list = Vehicle.objects.all().order_by('plate')
    return render(request, 'vehicles/vehicles_list.html', {'vehicles_list': vehicles_list}
                )

def add_vehicle(request):
    submitted = False
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.owner = request.user
            vehicle.save()
            return HttpResponseRedirect('/add_vehicle?submitted=True')

    else:
        form = VehicleForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'vehicles/add_vehicle.html',{'form': form, 'submitted': submitted})




def update_vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    form = VehicleForm(request.POST or None, instance=vehicle)
    if form.is_valid():
        vehicle = form.save(commit=False)
        vehicle.owner = request.user
        vehicle.save()
        return redirect('vehicles-list')

    return render(request, 'vehicles/update_vehicle.html', {'vehicle': vehicle, 'form': form})


def delete_vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    vehicle.delete()
    return redirect('vehicles-list')