from django.contrib import admin
from django.urls import path
from .views import (    
    agregar_familiar,
    familia_completa,
       
)

urlpatterns = [
path('add/<name>/<age>/<birthday>/', agregar_familiar),
path('familia_completa/', familia_completa),

]