
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blood/', views.blood, name='blood'),
    path('fireservice/', views.fire_service, name='fireservice'), 
    path('medicine/', views.medicine, name='medicine'),
    path('police_and_laywer/', views.police, name='police'), 
    path('help_post/', include('helppost.urls')),
    path('ambulance/', include('ambulance.urls')),
    path('fireservice/contact/', views.fire_service_call, name='fireservice_call'),
]
