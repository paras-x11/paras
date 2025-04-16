from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from home.models import *
from django.contrib import messages


# Create your views here.
def index(request):
    cars = Car.objects.all()
    context = {"cars": cars}
    return render(request, 'index.html', context)

def add_car(request):
    if request.method == "POST":
        data = request.POST 
        id = data.get('id')
        name = data.get('name')
        brand = data.get('brand')
        model_year = int (data.get('model_year'))
        price = data.get('price')
        fuel_type = data.get('fuel_type')
        transmission = data.get('transmission')
        color = data.get('color')
        mileage = data.get('mileage')
        # car_image = request.FILES.get('car_image')

        if not all ([name, brand, model_year, price, fuel_type, transmission, mileage]):
            messages.success(request, "All Fields are required!")
            return redirect("index")
        else:
            if id:
                car = Car.objects.get(pk=id)
                car.name=name
                car.brand=brand
                car.model_year=model_year
                car.price=price
                car.fuel_type=fuel_type
                car.transmission=transmission
                car.color=color
                car.mileage=mileage
                car.save()
                messages.success(request, "Car Updated Succesfully")
            else:
                car = Car.objects.create(name=name, brand=brand, model_year=model_year, price=price, 
                                        fuel_type=fuel_type, transmission=transmission, color=color, mileage=mileage)
                if car:
                    messages.success(request, "Car Added Succesfully")
                else:
                    messages.error(request, "Something Went Wrong, Please try Again!")
    return redirect("index")


def update_car(request, cid):
    car = Car.objects.get(pk=cid)
    cars = Car.objects.all()
    return render(request, "index.html", {"car": car, "cars": cars})


def delete_car(request, cid):
    car = Car.objects.get(pk=cid)
    car.delete()
    messages.success(request, "Car Deleted Succesfully")
    return redirect("index")