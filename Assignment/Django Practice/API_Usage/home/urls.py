from home import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('sendEmail', views.sendEmail, name='sendEmail'),
]
