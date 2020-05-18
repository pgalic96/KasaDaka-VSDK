from datetime import datetime

from django.db import models


# Create your models here.
from vsdk.service_development.models import SpokenUserInput


class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30, blank=None, null=None, default=None)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }


class Farmer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=200)
    house_nr = models.IntegerField()
    house_nr_extension = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=30, blank=None, null=None, default=None)

    def to_dict(self):
        return {
            'address': f'{self.street} {self.house_nr} {self.house_nr_extension}, '
                       f'{self.zipcode}',
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'street': self.street,
            'house_nr': self.house_nr,
            'house_nr_extension': self.house_nr_extension,
            'zipcode': self.zipcode,
            'phone_number': self.phone_number
        }


class Order(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    liters_of_milk = models.IntegerField()
    production_time = models.DateTimeField()
    arrival_time = models.DateTimeField(null=True, blank=True)
    valid = models.BooleanField(default=False)

    def to_dict(self):
        farmer = self.farmer.to_dict()
        driver = None
        if self.driver:
            driver = self.driver.to_dict()

        return {
            'id': self.id,
            'farmer': farmer,
            'driver': driver,
            'liters_of_milk': self.liters_of_milk,
            'production_time': datetime.strftime(self.production_time, '%Y-%m-%d %H:%m:%S') if self.production_time else '',
            'arrival_time': datetime.strftime(self.arrival_time, '%Y-%m-%d %H:%m:%S') if self.arrival_time else '',
            'valid': self.valid
        }
