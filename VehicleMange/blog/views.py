from django.shortcuts import HttpResponse, render
from django.http import HttpRequest
from .models import Person, Vehicle
from .forms import modifyform, vehicleModelForm

def hompage(request):
    vekVehicle = Vehicle.objects.all()
    vekPerson = Person.objects.all()
    context = {
        "VehicleModel" : vekVehicle,
        "memberName" : vekPerson,
        }
    return render(request, "homepage.html", context)

def vehicleDetail(request, carModel):
    carModel = Vehicle.objects.get(carModel = carModel)
    context = {
        "VehicleModel" : carModel
        }
    return render(request, "detail.html", context)

def returnVehicle(request) :
    modify = vehicleModelForm()
    if request.method == "POST": 
        modify = vehicleModelForm(request.POST)
        if modify.is_valid():
            modify.save()

    context = {
        "formkey" : modify
        }
    return render(request, "modify.html", context)


'''
def returnVehicle(request) :
    modify = modifyform()
    if request.method == "POST": 
        modify = modifyform(request.POST)
        if modify.is_valid():
            print("gooooood")
            if(modify.cleaned_data['carModel']=="Carnival" or "Seltos") :
                print("verygood")
                carModel = modify.cleaned_data['carModel']
                location = modify.cleaned_data['location']
                mileage = modify.cleaned_data['mileage']
                nowUser = modify.cleaned_data['NowUser']

    context = {
        "formkey" : modify
        }
    return render(request, "modify.html", context)
# Create your views here.
'''
