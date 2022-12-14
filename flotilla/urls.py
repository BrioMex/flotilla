from django.urls import path

from . import views #importing views for vehicles app

urlpatterns = [
    path('', views.home, name = "home"), #first: defining url in browser, second: function or class name, third name assigned ofr easy calling
    path('vehicles/', views.all_vehicles, name= "vehicles-list"),
    path('add_vehicle', views.add_vehicle, name= "add-vehicle"),
    path('update_vehicle/<int:vehicle_id>/', views.update_vehicle, name= "update-vehicle"),
    path('delete_vehicle/<int:vehicle_id>/', views.delete_vehicle, name = 'delete-vehicle'),
]
