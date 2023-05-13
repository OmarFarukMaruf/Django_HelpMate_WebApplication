from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.blood, name='help_post'),
    path('post/', views.post, name= 'post')
   
]


