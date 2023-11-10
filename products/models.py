from django.db import models

# Create your models here.
# product model


class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    # function = models.ForeignKey(Functie, on_delete=models.SET_NULL, null=True, blank=True)
    
    # def __str__(self):
    #     return self.name
    
# category model
