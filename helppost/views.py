from django.shortcuts import render
from .form import HelpForm
from .models import HelpPost

# Create your views here.
def help_post(request):
    help_post = HelpPost.objects.all()  
    context = {
        'help_post' : help_post,
    }
    return render(request, 'help_post.html', context)


def post(request):
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
    else:
        form = HelpForm()

    return render(request, 'post_help.html', {'form': form})