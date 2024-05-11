from django.db import models

# Create your models here.

class Order(models.Model):
    Name= models.CharField(max_length=50)
    Phone_Number= models.TextField()
    Email= models.TextField()
    Address= models.TextField()
    def __str__(self):
        return f"{self.Name}"

class Cart(models.Model):
    Dish= models.CharField(max_length=100)
    Price= models.TextField()
    Quantity = models.TextField()
    def __str__(self):
        return f"{self.Dish}"

class Dishes(models.Model):
    Dishname= models.CharField(max_length=100)
    Price= models.TextField()
    Image= models.FileField()
    def __str__(self):
        return f"{self.Dishname}"
    
class dishes:
    dishnames: str
    dishprice: int
    img: str