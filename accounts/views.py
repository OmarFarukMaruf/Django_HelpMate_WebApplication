from django.shortcuts import render
from .forms import RagistrationForm
from .models import CustomUser
from django.contrib import messages, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RagistrationForm(request.POST)
        if form.is_valid():
            frist_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            passwors = form.cleaned_data['password']
            username = email.split("@")[0]
            user = CustomUser.objects.create_user(email = email, first_name = frist_name, last_name = last_name, username=username)
            user.phone = phone
            user.save()
            messages.success(request, "Registration Successful")
    else:
        form = RagistrationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/register.html', context)
