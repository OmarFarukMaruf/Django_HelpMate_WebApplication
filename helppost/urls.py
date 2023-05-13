from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.help_post, name='help_post'),
    path('post/', views.post, name= 'post')
   
]
