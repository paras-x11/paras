from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import StudentSerializer
from api.models import *


# Create your views here.
@api_view(['GET'])
def getStudents(request):
    allstudents = Student.objects.all()
    s_data = StudentSerializer(allstudents,     many=True)
    print(s_data)
    return Response(data = s_data.data)

@api_view(['POST'])
def addStudent(request):
    serialize_data = StudentSerializer(data = request.data)
    if not serialize_data.is_valid():
        return Response({'status':'202','errors':serialize_data.errors,'message':"something went wrong"})
    serialize_data.save()
    return HttpResponse("post req called")

def updateStudent(request):
    pass

def deleteStudent(request):
    pass