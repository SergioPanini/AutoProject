from django.shortcuts import render
from django.http import HttpResponse
from .models import Users, Numbers, Parks, SecretTokens
# Create your views here.

SecretTokenApp = '1234'

def ShowMainPage(request):
    return render(request, 'MainPage.html', context = {})

def IsUser(request):
    try:

        if request.method == 'GET' and request.GET['SecretToken'] == SecretTokenApp:
                return HttpResponse(Users.objects.filter(idTelegram=request.GET['idtelegram']).exists())
        
        else:
            return HttpResponse('Errors')
    
    except: 
        return HttpResponse(' Errors in get parameters')


def AddUser(request):
    try:

        if request.method == 'GET' and request.GET['SecretToken'] == SecretTokenApp:
                NewUser = Users.objects.create(Name=request.GET['name'], Surname=request.GET['surname'], idTelegram=request.GET['idtelegram'], MobileNumber=request.GET['mobilenumber'])
                return HttpResponse('True')
        
        else:
            return HttpResponse('Errors')
    
    except: 
        return HttpResponse(' Errors in get parameters')

def test(request):
    NewUser = Users.objects.create(Name=request.GET['name'], Surname=request.GET['surname'], idTelegram=request.GET['idtelegram'], MobileNumber=request.GET['mobilenumber'])
                
    return HttpResponse('true')
'''
def AddUser(request, Name, Surname, CarNumber, NameCarNumber, CallNumber, idTelegram, SecretToken):
    if SecretToken == SecretTokenApp:
        NewUser = Users(Name=Name, Surname=Surname,MobileNumber=CallNumber, idTelegram=idTelegram)
        NewUser.save()
        NewUser.numbers_set.create(NumberName=NameCarNumber, CarNumber=CarNumber)
        return HttpResponse('True')

def EditUserData(request, idTelegram, Field, Value, SecretToken):
    if SecretToken == SecretTokenApp:
        SelectUser = Users.objects.get(idTelegram=idTelegram)
       
        if Field == 'Name':
            SelectUser.Name = Value
        elif Field == 'Surname':
            SelectUser.Surname = Value
        elif Field == 'MobileNumber':
            SelectUser.MobileNumber = Value
        else: return HttpResponse('Error, Field not found')

        SelectUser.save()
    return HttpResponse('edit data')

#def ShowAllNumbers(request):
#    CarNumbersAll = CarNumbers.objects.all()
#    return render(request, 'index.html',context = {'ListUsers' : CarNumbersAll})
'''