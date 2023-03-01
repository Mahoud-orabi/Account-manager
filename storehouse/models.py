from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.text import slugify
# Create your models here.
class Store(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(unique=True)
    created_dt=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        super().save(*args, **kwargs)

class Category(models.Model):
    store=models.ForeignKey(Store,related_name='store',on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    count=models.IntegerField(validators=[MaxValueValidator(100)])
    created_dt=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name