from django.contrib import admin
from .models.product import Product
from .models.category import category

# Register your models here.
admin.site.register(Product)
admin.site.register(category)
