from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import BadHeaderError, send_mail
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request , "index.html")

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def sendEmail(request):
    context = {"result": "Invalid request"}  # Default response

    if request.method == 'POST':
        address = request.POST.get("address")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if not address or not subject or not message:
            return HttpResponse("Fill All The Details")

        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
            context["result"] = "Email sent successfully"
        except Exception as e:
            context["result"] = f"Error sending email: {e}"

    return HttpResponse(context["result"])  # Always return a valid response
