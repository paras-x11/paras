from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def _1(request):
    return render(request, "1.html")

def doc_profile(request):
    context = {
        'doctor': {
            'name': 'Dr. Jane Smith',
            'specialization': 'Cardiology',
            'experience': '10 years',
            'contact': '+1 (555) 123-4567',
            'email': 'jane.smith@example.com',
            'bio': 'Dr. Jane Smith is an experienced cardiologist specializing in advanced cardiac care. She is passionate about helping her patients live healthier lives.',
        }
    }
    return render(request, 'doc_profile.html', context)
