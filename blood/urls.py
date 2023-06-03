from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.blood, name='blood'),
    path('massage/', views.blood_post, name= 'massage')
   
]


