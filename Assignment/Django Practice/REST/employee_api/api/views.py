from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import EmployeeSerializer
from api.models import *


# Create your views here.
@api_view(['GET'])
def getEmployees(request):
    allemployees = Employee.objects.all()
    e_data = EmployeeSerializer(allemployees, many=True)
    return Response(e_data.data)

@api_view(['POST'])
def addEmployees(request):
    serialize_data = EmployeeSerializer(data = request.data)
    if not serialize_data.is_valid():
        return Response({'status':'202','errors':serialize_data.errors,'message':"something went wrong"})
    serialize_data.save()
    return HttpResponse("post called")