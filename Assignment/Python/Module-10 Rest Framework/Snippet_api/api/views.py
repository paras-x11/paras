from django.shortcuts import render, get_object_or_404
from api.models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from api.serializer import *


# Create your views here.
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def snippets(request):
    try:
        if request.method == "GET":
            snippets = Snippet.objects.all()
            s_snippets = SnippetSerializer(snippets, many=True)
            return Response({"Snippets": s_snippets.data}, status=status.HTTP_200_OK)
        
        if request.method == "POST":
            s_snippet = SnippetSerializer(data=request.data)
            if not s_snippet.is_valid():
                return Response({"status":"400", "errors":s_snippet.errors, "message":"Validation failed!, check input!"}, status=status.HTTP_400_BAD_REQUEST)
            s_snippet.save()
            return Response({"message":"Snippet Added Successfully", "data":s_snippet.data}, status=status.HTTP_201_CREATED)
   
    except Exception as e:
        return Response({"errors": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['PATCH', 'DELETE'])
# @permission_classes([IsAuthenticated])
def modifySnippet(request, id):
    try:
        snippet = get_object_or_404(Snippet, pk=id)

        if request.method == "PATCH":
            s_snippet = SnippetSerializer(snippet, data=request.data)
            if not s_snippet.is_valid():
                return Response({"errors":s_snippet.errors, "message":"Validation failed!, check input!"}, status=status.HTTP_400_BAD_REQUEST)
            s_snippet.save()
            return Response({"message":"Snippet Updated Successfully", "data":s_snippet.data}, status=status.HTTP_200_OK) 
        
        if request.method == "DELETE":
            s_snippet = SnippetSerializer(snippet, data=request.data)
            snippet.delete()
            return Response({"message":"Snippet Deleted Successfully", "data":s_snippet.data}, status=status.HTTP_200_OK) 
        
    except Exception as e:
        return Response({"errors": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    