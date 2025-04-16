
from django.urls import path
from tbd_app.views import *


urlpatterns = [
    path("", index, name="index"),
    path("index/", index, name="index"),
    path("add_car/", add_car, name="add_car"),
]
