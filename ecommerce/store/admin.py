from django.contrib import admin
from store.models import * 

# Register your models here.

admin.site.register((Customer, Order, Product, ShippingAddress, OrderItem))