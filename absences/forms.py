from django import forms
from .models import *

class AddPersonForm(forms.ModelForm):
    class Meta:
        model=Person
        exclude=['slug',]

class AddDetailsForm(forms.ModelForm):
    class Meta:
        model=Day
        fields=['absences',]

# class UpdateDetails(forms.ModelForm):
#     class Meta:
#         model=Day
#         fields=['absences',]
