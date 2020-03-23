from django.db import models

# Create your models here.

class Users(models.Model):
    Name = models.CharField(max_length=255)
    Surname = models.CharField(max_length=255)
    idTelegram = models.CharField(max_length=255)
    MobileNumber =models.CharField(max_length=255)

class Numbers(models.Model):
    idUser = models.ForeignKey(Users, on_delete=models.CASCADE)
    NumberName = models.CharField(max_length=255)
    CarNumber = models.CharField(max_length=255)

class Parks(models.Model):
    idNumber = models.ForeignKey(Numbers,on_delete=models.CASCADE)
    DateInput = models.DateTimeField()
    DateOutput = models.DateTimeField()
    Pay = models.BooleanField(default=False)

class SecretTokens(models.Model):
    NameApp = models.CharField(max_length=255)
    SecretToken = models.CharField(max_length=255)