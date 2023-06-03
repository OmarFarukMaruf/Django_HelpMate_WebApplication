from django import forms
from .models import HelpPost


class HelpForm(forms.ModelForm):
    class Meta:
        model = HelpPost
        fields = ('name', 'district', 'city', 'address',
                  'post', 'phone_number', 'image', 'emergency')
