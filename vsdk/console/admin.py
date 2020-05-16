# Register your models here.
from django.contrib import admin


# Register your models here.
from .models import Order, Driver, Farmer

admin.site.register(Driver)
admin.site.register(Order)
admin.site.register(Farmer)
