from django.db import models

# Create your models here.

class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30, blank=None, null=None, default=None)

class Farmer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=200)
    house_nr = models.IntegerField()
    house_nr_extension = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=30, blank=None, null=None, default=None)

class Order(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    liters_of_milk = models.IntegerField(null=True)
    production_time = models.DateTimeField(null=True)
    arrival_time = models.DateTimeField(null=True, blank=True)