from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view
from rest_framework import status
from api.models import *
from api.serializer import *

# Create your views here.
@api_view(['GET'])
def getUsers(request):
    try:
        users = User.objects.all()
        s_users = UserSerializer(users, many=True)  # Serialize multiple users
        return Response({"users": s_users.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def registerUser(request):
    try:
        s_user = UserSerializer(data=request.data)
        if not s_user.is_valid():
            return Response({"data_errors": s_user.errors}, status=status.HTTP_400_BAD_REQUEST)
        user = s_user.save()

        token = Token.objects.get(user=user)                    # Fetch the existing token (ensure one token per user)
        return Response({"message": "User registered successfully!", "token": token.key}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'errors': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryAPI(APIView):
    def get(self, request):
        try:
            categories = Category.objects.all()
            s_categories = Categoryserializer(categories, many=True)
            return Response({"categories": s_categories.data})
        except Exception as e:
            return Response({"errors":s_categories.errors})