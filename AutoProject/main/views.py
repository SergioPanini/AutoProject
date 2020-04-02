from django.shortcuts import render
from django.http import HttpResponse
from .models import Users, Numbers, Parks, SecretTokens
from django.utils import timezone
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


def AddNumber(request):
    try:

        if request.method == 'GET' and request.GET['SecretToken'] == SecretTokenApp:
                Select_User = Users.objects.get(idTelegram=request.GET['idtelegram'])
                New_CarNumber = Numbers.objects.create(idUser=Select_User, NumberName=request.GET['numbername'], CarNumber=request.GET['carnumber'])
                return HttpResponse('True')
        
        else:
            return HttpResponse('Errors')
    
    except: 
        return HttpResponse(' Errors in get parameters')

def AddParksIn(request):
    try:

        if request.method == 'GET' and request.GET['SecretToken'] == SecretTokenApp:
            Select_CarNumber = Numbers.objects.get(CarNumber=request.GET['carnumber'])
            New_Parks = Parks.objects.create(idNumber=Select_CarNumber, DateInput=timezone.now(), DateOutput='2000-01-01 00:00:00', Pay='False')
            return HttpResponse('True')
        
        else:
            return HttpResponse('Errors')
    
    except: 
        return HttpResponse(' Errors in get parameters')


def AddParksOut(request):
    try:

        if request.method == 'GET' and request.GET['SecretToken'] == SecretTokenApp:
            Select_CarNumber = Numbers.objects.get(CarNumber=request.GET['carnumber'])
            New_Parks = Parks.objects.filter(idNumber=Select_CarNumber).update(DateOutput=timezone.now())
            return HttpResponse('True')
        
        else:
            return HttpResponse('Errors')
    
    except: 
        return HttpResponse(' Errors in get parameters')

def EditName(request):
    try:

        if request.method == 'GET' and request.GET['SecretToken'] == SecretTokenApp:
            Select_User = Users.objects.get(idTelegram=request.GET['idtelegram'])
            Select_User.Name = request.GET['newname']
            Select_User.save()                                       
            return HttpResponse('True')
        
        else:
            return HttpResponse('Errors')
    
    except: 
        return HttpResponse(' Errors in get parameters')

def EditPhone(request):
    try:

        if request.method == 'GET' and request.GET['SecretToken'] == SecretTokenApp:
            Select_User = Users.objects.get(idTelegram=request.GET['idtelegram'])
            Select_User.MobileNumber = request.GET['newphone']
            Select_User.save()                                       
            return HttpResponse('True')
        
        else:
            return HttpResponse('Errors')
    
    except: 
        return HttpResponse(' Errors in get parameters')

def EditCarNumber(request):
    try:

        if request.method == 'GET' and request.GET['SecretToken'] == SecretTokenApp:
            User = Users.objects.filter(idTelegram=request.GET['idtelegram'])
            Number = Numbers.objects.filter(idUser__in=User, CarNumber=request.GET['number']).update(CarNumber = request.GET['newnumber'])
                            
            return HttpResponse('True')
        
        else:
            return HttpResponse('Errors')
    
    except: 
        return HttpResponse(' Errors in get parameters')

def EditCarName(request):
    try:

        if request.method == 'GET' and request.GET['SecretToken'] == SecretTokenApp:
            User = Users.objects.filter(idTelegram=request.GET['idtelegram'])
            Number = Numbers.objects.filter(idUser__in=User, CarNumber=request.GET['carnumber']).update(NumberName = request.GET['newname'])

            return HttpResponse('True')
        
        else:
            return HttpResponse('Errors')
    
    except: 
        return HttpResponse(' Errors in get parameters')

def GetStatus(request):
    try:

        if request.method == 'GET' and request.GET['SecretToken'] == SecretTokenApp:
            Data = {'CarName':'', 'CarNumber':'', 'OUT':'', 'DeltaTime':''}
            Select_User = Users.objects.filter(idTelegram=request.GET['idtelegram'])
            Select_CarNumbers = Numbers.objects.filter(idUser__in=Select_User)
            Select_Parks = Parks.objects.filter(idNumber__in=Select_CarNumbers).order_by('-DateInput')
    
            if Select_Parks.count() == 0:
                return HttpResponse('Parks is not')
            else:
                print('select_parks', Select_Parks[0])
                print('select_number', Select_CarNumbers)
                                
                Data['CarName'] = Select_Parks[0].idNumber.NumberName
                Data['CarNumber'] = Select_Parks[0].idNumber.CarNumber
                print('outDate', Select_Parks[0].DateOutput)
                if str(Select_Parks[0].DateOutput) == '2000-01-01 00:00:00+00:00':
                    Data['OUT'] = False
                    Data['DeltaTime'] = str(timezone.now()- Select_Parks[0].DateInput)
                
                else:
                    Data['OUT'] = True         
                    Data['DeltaTime'] = str(Select_Parks[0].DateOutput - Select_Parks[0].DateInput)
                
                return HttpResponse(str(Data))
        else:
           return HttpResponse('Errors')
    
    except: 
        return HttpResponse('Errors in get parameters')


def test(request):
    User = Users.objects.filter(idTelegram=request.GET['idtelegram'])
    Number = Numbers.objects.filter(idUser__in=User, CarNumber=request.GET['carnumber']).update(NumberName = request.GET['newname'])
    
    return HttpResponse('true') 