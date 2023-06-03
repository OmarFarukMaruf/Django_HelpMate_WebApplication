from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def fire_service(request):
    return render(request, 'fireservice/fireservice.html')

def fire_service_call(request):
    return render(request, 'fireservice/fireservice_numberlist.html')

def medicine(request):
    return render(request, 'medicine.html')

def police(request):
    return render(request, 'police.html')

def login(request):
    return render(request, 'singin.html')

def register(request):
    return render(request, 'register.html')