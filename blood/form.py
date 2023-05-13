from django import forms
from .models import BloodModel

class BloodForm(forms.ModelForm):
    class Meta:
        model = BloodModel
        fields = ('name', 'district', 'city', 'area','blood_group', 'phone_number', 'comment')