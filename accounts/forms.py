from django import forms
from .models import Clients,Categories,List
class AddClient(forms.ModelForm):
    class Meta:
        model= Clients
        fields=['f_name','l_name',]
        labels={
            "f_name":"First Name",
            'l_name':'Last Name'
        }

class AddCategory(forms.ModelForm):
    class Meta:
        model=Categories
        fields=['name','item_number']
        labels={
            'name':'Name'
        }

class AddList(forms.ModelForm):
    class Meta:
        model=List
        fields=['name','count','time','num_motor']
        labels={
            'num_motor':'Number of motors'
        }