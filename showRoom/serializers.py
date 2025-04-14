from rest_framework import serializers
from .models import Sales, Customer, Car, Category


# Sales Serializer
class SalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = ['customer', 'car_title', 'payment_method', 'total_price']

# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']


# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']


# Car Serializer
class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['price', 'title', 'color', 'available', 'car_modal', 'category']



