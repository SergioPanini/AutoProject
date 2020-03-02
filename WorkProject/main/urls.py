from django.urls import path
from . import views

urlpatterns = [
    path('ShowAllNumbers/', views.ShowAllNumbers),
    path('AddNumber/<str:Name>/<str:Surname>/<str:CarNumber>/<str:Country>/<str:TelegramId>/<str:SecretToken>', views.AddNumber),
    path('EditRecord/<str:NameRecord>/<str:SecretToken>/',views.EditRecord),
]