from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowMainPage),
    path('isuser/', views.IsUser),
    path('adduser/', views.AddUser),
    path('addnumber/', views.AddNumber),
    path('addparksin/', views.AddParksIn),
    path('addparksout/', views.AddParksOut),

    path('editname/', views.EditName),
    path('editphone/', views.EditPhone),
    path('parksin/', views.AddParksIn),
    path('parksout/', views.AddParksOut),
    #path('editcarnumber/', views.EditCarNumber),
    path('getstatus/', views.GetStatus),
    path('test/', views.test),
]
    