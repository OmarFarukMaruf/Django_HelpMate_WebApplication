
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('account/', include('accounts.urls')),
    path('blood/', include('blood.urls')),
    path('fireservice/', views.fire_service, name='fireservice'), 
    path('medicine/', views.medicine, name='medicine'),
    path('police_and_laywer/', views.police, name='police'), 
    path('help_post/', include('helppost.urls')),
    path('ambulance/', include('ambulance.urls')),
    path('fireservice/contact/', views.fire_service_call, name='fireservice_call'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
