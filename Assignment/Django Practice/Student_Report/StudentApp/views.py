from django.shortcuts import render
from StudentApp.models import *

# Create your views here.
def index(request):
    return render(request, "index.html")