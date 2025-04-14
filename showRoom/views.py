from django.db.migrations import serializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Car, Customer
from .serializers import CarSerializer, CustomerSerializer, SalesSerializer

class CreateCarView(APIView):
    def post(self, request, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListCarView(APIView):
    def get(self, request, format=None):
        cars = Car.objects.all()

        serializer = CarSerializer(cars, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteCarView(APIView):
    def delete(self, request, id, format=None):
        car = Car.objects.filter(id=id)
        car.delete()

        return Response({"detail": "Car deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class CustomerView(APIView):
    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerListView(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



# class CutomerDelete
class PurchaseCarView(APIView):
    def post(self, request, format=None):
        car_id = request.data.get('car')
        customer_id = request.data.get('customer')
        payment_method = request.data.get('payment_method')

        try:
            car = Car.objects.get(id=car_id)
        except Car.DoesNotExist:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

        if not car.available:
            return Response({"error": "Car is not available"}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare sales data
        sales_data = {
            'customer': customer.id,
            'car': car.id,  # use the updated field name
            'payment_method': payment_method,
            'total_price': car.price  # handled on server
        }

        serializer = SalesSerializer(data=sales_data)
        if serializer.is_valid():
            serializer.save()

            # Update car availability
            car.available = False
            car.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
