from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('', views.ambulance, name='ambulance'),
    path('contact/', views.ambulance_number, name='ambulance_number')

]
