from django.contrib import admin
from .models import Order, Product, Inventory, InventoryStock

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(InventoryStock)
