from django.shortcuts import render
from django.http import HttpResponse
from .models import Cards, CarNumbers
# Create your views here.

SECRETTOKEN = '3443'

def ShowAllNumbers(request):
    CarNumbersAll = CarNumbers.objects.all()
    return render(request, 'index.html',context = {'ListUsers' : CarNumbersAll})

def AddNumber(request, Name, Surname, CarNumber, Country, TelegramId, SecretToken):
    if SecretToken == SECRETTOKEN:
        New_record = CarNumbers(Name=Name, Surname=Surname, CarNumber=CarNumber, Country=Country, TelegramId=TelegramId)
        try:
            New_record.save()
            return HttpResponse('Record is add')
        except:
            return HttpResponse('Record is not add')
    else: return HttpResponse('Token is not valid')