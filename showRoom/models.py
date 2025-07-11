from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class CustomUser(AbstractUser):  # Extend the default User model
    is_admin = models.BooleanField(default=False)  # To identify admin users
    is_customer = models.BooleanField(default=True)  # To identify customer users

    def __str__(self):
        return self.username

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

# Car Model
class Car(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    car_modal = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.car_modal} ({self.color})"

# Customer Model (Linked to CustomUser)
class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="customer_profile")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Sales Model
class Sales(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_of_sale = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    payment_method = models.CharField(max_length=50)
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"Sale to {self.customer.first_name} {self.customer.last_name} on {self.date_of_sale}"
