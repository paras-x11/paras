from django.contrib import admin
from django.urls import path
from api.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("loginUser/", obtain_auth_token, name="loginUser"),
    path("registerUser/", registerUser, name="registerUser"),

    path("getUsers/", getUsers, name="getUsers"),

    path("categories", CategoryAPI.as_view())
]
