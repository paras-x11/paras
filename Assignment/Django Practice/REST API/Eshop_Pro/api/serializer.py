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

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['category'] = CategorySerializer(instance.category).data
        return resp

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"

    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['user'] = UserSerializer(instance.user).data
        return resp
    
class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = "__all__"
    
    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['cart'] = CartSerializer(instance.cart).data
        resp['product'] = ProductSerializer(instance.product).data
        return resp 