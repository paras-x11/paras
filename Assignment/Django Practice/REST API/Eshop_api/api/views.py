from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import *
from api.models import *

# Create your views here.

# -> CATOGORIES:
@api_view(['GET'])
def getCategories(request):
    return HttpResponse("get category called")

@api_view(['POST'])
def addCategory(request):
    return HttpResponse("add category called")

@api_view(['PATCH'])
def updateCategory(request, id):
    return HttpResponse(f"{id} update category called")

@api_view(['DELETE'])
def deleteCategory(request, id):
    return HttpResponse(f"{id} delete category called")


# -> PRODUCTS:
@api_view(['GET'])
def getProducts(request):
    return HttpResponse("get Product called")

@api_view(['POST'])
def addProduct(request):
    return HttpResponse("add Product called")

@api_view(['PATCH'])
def updateProduct(request, id):
    return HttpResponse(f"{id} update Product called")

@api_view(['DELETE'])
def deleteProduct(request, id):
    return HttpResponse(f"{id} delete Product called")
