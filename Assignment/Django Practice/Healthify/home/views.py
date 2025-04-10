from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from home.models import *
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def get_user_info(request):
    user = request.user
    if user.is_anonymous:
        return JsonResponse({'name': 'Newbie'})
    
    name = ""
    role = ""

    if user.is_doctor:
        try:
            doctor = DoctorProfile.objects.get(user=user)
            name = doctor.full_name
            role = "Doctor"
        except DoctorProfile.DoesNotExist:
            name = "Doctor" 

    if user.is_patient:
        try:
            patient = PatientProfile.objects.get(user=user)
            name = patient.full_name
            role = "Patient"
        except DoctorProfile.DoesNotExist:
            name = "Patient"

    if user.is_superuser:
        name = f"{user.first_name} {user.last_name}"
    print(name, role)
    return JsonResponse({'name':name, "role": role})

def doctors(request):
    doctors = DoctorProfile.objects.all()
    context = {'doctors': doctors}
    return render(request, "doctors.html", context)

def patient_list(request):
    return render(request, "patient_list.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def testimonial(request):
    return render(request, "testimonial.html")

def contact(request):
    return render(request, "contact.html")

@login_required(login_url='login_user')
def appointment(request):
    return render(request, "appointment.html")

@login_required(login_url='login_user')
def appointment_detail(request):
    return render(request, "appointment_detail.html")

def doctor_profile(request):
    return render(request, "doctor_profile.html")

def profile(request):
    return render(request, "profile.html")

def signup_user(request):
    try:
        if request.method == "POST":
            role = request.POST.get('role')
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')

            is_email_exist = User.objects.filter(email=email)
            if is_email_exist:
                return render(request, 'signup.html', {"message":'Email already exist !!'})
            
            user = User.objects.create_user(
                email=email,
                password=password,
                is_doctor=(role == "Doctor"),
                is_patient=(role == "Patient")
            )

            if role == "Doctor":
                doctor = DoctorProfile.objects.create(user=user, first_name=fname, last_name=lname, phone=phone)
                print(doctor)
            if role == "Patient":
                patient = PatientProfile.objects.create(user=user, first_name=fname, last_name=lname, phone=phone)
                print(patient)

            return render(request, "login.html", {"message": f'{role} Registration Succesfull, Login Now!!'})
        return render(request, "signup.html")
    except Exception as e:
        return render(request, 'signup.html', {"message": str(e)})

def login_user(request):
    try:
        if request.method=="POST":
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect(index)
            else:
                return render(request, 'login.html', {"message": 'Invalid Credential !! '})

        return render(request, "login.html")
    except Exception as e:
        return render(request, 'login.html', {"messgae": str(e)})
    
@login_required(login_url='login_user')
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'login.html', {'message': "Logout Succesfull"})
    else:
        return render(request, 'index.html')

    