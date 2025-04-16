from django.shortcuts import render, redirect
from tbd_app.models import *

# Create your views here.
def index(request):
    cars = Car.objects.all()
    return render(request, "index.html", {"cars": cars})

def add_car(request):
    return redirect("index")