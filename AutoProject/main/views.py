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



def GetStatus(request):
    try:

        if request.method == 'GET' and request.GET['SecretToken'] == SecretTokenApp:
            Data = {'CarName':'', 'CarNumber':'', 'OUT':'', 'DeltaTime':''}
            Select_User = Users.objects.get(idTelegram=request.GET['idtelegram'])
            Select_CarNumbers = Numbers.objects.filter(idUser=Select_User)
            Select_Parks = Parks.objects.filter(idNumber__in=Select_CarNumbers).order_by('-DateInput')
    
            if Select_Parks.count() == 0:
                return HttpResponse('Parks is not')
            else:
                print('select_parks', Select_Parks[0])
                print('select_number', Select_CarNumbers)
                        
                Data['DeltaTime'] = str(Select_Parks[0].DateOutput - Select_Parks[0].DateInput)
                Data['CarName'] = Select_Parks[0].idNumber.NumberName
                Data['CarNumber'] = Select_Parks[0].idNumber.CarNumber
                print(Select_Parks[0].DateOutput)
                if str(Select_Parks[0].DateOutput) == '2000-01-01 00:00:00+00:00':
                    Data['OUT'] = False
                else:
                    Data['OUT'] = True 
            
            
                return HttpResponse(str(Data))
        else:
            return HttpResponse('Errors')
    
    except: 
        return HttpResponse('Errors in get parameters')


def test(request):
    Select_User = Users.objects.get(idTelegram=request.GET['idtelegram'])
    Select_CarNumbers = Numbers.objects.filter(idUser=Select_User)
    Select_Parks = Parks.objects.filter(idNumber__in=Select_CarNumbers).order_by('-DateInput').values()
    return HttpResponse(Select_Parks)
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