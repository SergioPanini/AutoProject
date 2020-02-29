from django.shortcuts import render
from django.http import HttpResponse
from .models import Cards, CarNumbers
# Create your views here.

def ShowAllNumbers(request):
    CarNumbersAll = CarNumbers.objects.all()
    return render(request, 'index.html',context = {'ListUsers' : CarNumbersAll})