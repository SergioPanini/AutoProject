from django.db import models

# Create your models here.

class CarNumbers(models.Model):
    Name = models.CharField(max_length = 255)
    Surname = models.CharField(max_length = 255)
    CarNumber = models.CharField(max_length = 9)
    Country = models.CharField(max_length = 3)

class Cards(models.Model):
    id_user = models.ForeignKey(CarNumbers, on_delete = models.CASCADE)
    NumberCard = models.IntegerField()
    Date = models.IntegerField()
    CVC = models.IntegerField()
