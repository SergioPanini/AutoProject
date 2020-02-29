from django.urls import path
from . import views

urlpatterns = [
    path('ShowAllNumbers/', views.ShowAllNumbers),

]