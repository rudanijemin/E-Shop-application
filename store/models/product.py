from django.db import models
from .category import category   
 


class Product(models.Model):
    name = models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(category, on_delete=models.CASCADE, default=1)
    description=models.CharField(max_length=280,default=" ")
    image=models.ImageField(upload_to="uploads/products/")

    def __str__(self):
        return self.name
    
