from django.shortcuts import render, HttpResponse

# Create your views here.

def demo(request):
    context = {
        "variable" : "I am variable 007",
        "variable1" : "Paras",
        "variable2" : "Rana"
    }
    return render(request, 'demo.html', context)
    # return HttpResponse("HELLO WORLD! \n \n Index Page")

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("HELLO WORLD! \n \n Index Page")

def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is services page")

def contact(request):
    return HttpResponse("This is contact page")

