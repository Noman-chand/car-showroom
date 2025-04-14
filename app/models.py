from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(blank=True, null=True)
    # gender = models.IntegerField(max_length=20,blank=True, null=True)