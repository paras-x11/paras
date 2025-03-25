from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import *
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create the user
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        token, _ = Token.objects.get_or_create(user=user)               # Ensure only one token per user
        return user

class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"