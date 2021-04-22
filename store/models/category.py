from django.db import models 

class category(models.Model):
    name = models.CharField(max_length=50)