from django.shortcuts import render
from .form import BloodForm
from .models import BloodModel

# Create your views here.

def blood(request):
    blood_post = BloodModel.objects.all()
    context = {
        'blood_post' : blood_post
    }
    return render(request, 'blood/blood_donation.html', context)

def blood_post(request):
    if request.method == 'POST':
        blood_form = BloodForm(request.POST)
        if blood_form.is_valid():
            blood_form.save()  # Save the form data to the database
    else:
        blood_form = BloodForm()

    return render(request, 'blood/donte.html', {'blood_form': blood_form})