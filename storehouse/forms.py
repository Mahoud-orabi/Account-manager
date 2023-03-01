from django import forms
from .models import *

class StoreForm(forms.ModelForm):
    class Meta:
        model=Store
        fields=['name',]

class DetailsForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','count']
