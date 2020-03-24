from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowMainPage),
    path('isuser/', views.IsUser),
    path('adduser/', views.AddUser),
    path('addnumber/', views.AddNumber),
    path('test/', views.test),
#    path('AddUser/<str:Name>/<str:Surname>/<str:CarNumber>/<str:NameCarNumber>/<str:CallNumber>/<str:idTelegram>/<str:SecretToken>/', views.AddUser),
#    path('EditUserData/<str:idTelegram>/<str:Field>/<str:Value>/<str:SecretToken>/', views.EditUserData),
#    path('EditCarNumberData/<str:idTelegram>/<str:Field>/<str:Value>/<str:SecretToken>/', views.EditCarNumberData)
]
    