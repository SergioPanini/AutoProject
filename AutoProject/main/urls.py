from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowMainPage),
    path('isuser/', views.IsUser),
    path('adduser/', views.AddUser),
    path('addnumber/', views.AddNumber),
    path('addparksin/', views.AddParksIn),
    path('addparksout/', views.AddParksOut),
    path('test/', views.test),
]
    