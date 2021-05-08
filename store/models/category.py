from django.db import models 

class category(models.Model):
    name = models.CharField(max_length=50)

    
    @staticmethod
    def get_all_categories():
        return category.objects.all()

    def __str__(self): 
        return self.name
