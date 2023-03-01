from django.db import models
from django.utils.text import slugify
# Create your models here.
class Person(models.Model):
    f_name=models.CharField(max_length=50,unique=True)
    l_name=models.CharField(max_length=50)
    slug=models.SlugField(unique=True)
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.f_name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.f_name

class Day(models.Model):
    person=models.ForeignKey(Person,related_name='day',on_delete=models.CASCADE)
    absences=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.absences

