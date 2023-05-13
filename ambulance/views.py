from django.shortcuts import render

# Create your views here.
def ambulance(request):
    return render(request, 'ambulance/ambulance.html')

def ambulance_number(request):
    return render(request, 'ambulance/ambulance_number.html')