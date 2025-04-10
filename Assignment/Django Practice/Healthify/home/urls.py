"""
URL configuration for Healthify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('index', index, name="index"),
    path('doctors', doctors, name="doctors"),
    path('about', about, name="about"),
    path('services', services, name="services"),
    path('contact', contact, name="contact"),
    path('appointment', appointment, name="appointment"),
    path('testimonial', testimonial, name="testimonial"),
    path('doctor_profile', doctor_profile, name="doctor_profile"),
    path('patient_list', patient_list, name="patient_list"),
    path('appointment_detail', appointment_detail, name="appointment_detail"),
    path('profile', profile, name="profile"),
    path('get_user_info', get_user_info, name="get_user_info"),
    path('signup_user', signup_user, name="signup_user"),
    path('login_user', login_user, name="login_user"),
    path('logout', logout_user, name="logout"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)