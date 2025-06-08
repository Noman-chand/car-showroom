from rest_framework import serializers
from .models import Sales, Customer, Car, Category

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['customer', 'car', 'payment_method', 'total_price']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone_number', 'address']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['price', 'title', 'color', 'available', 'car_modal', 'category']
