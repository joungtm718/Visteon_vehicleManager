from django.urls import path
from .views import hompage, vehicleDetail, returnVehicle

app_name = "homepage"

urlpatterns = [
    path('', hompage),
    path('make/', returnVehicle),
    path('<carModel>/',vehicleDetail)
]