from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

class Clients(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    f_name=models.CharField(max_length=50,unique=True)
    l_name=models.CharField(max_length=50)
    created_dt=models.DateTimeField(auto_now_add=True)
    created_by=models.CharField(null=True,max_length=50)
    slug=models.SlugField(unique=True)
    
    def save(self,*args, **kwargs ):
        self.slug=slugify(self.f_name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.f_name
    
    def get_last_category(self):
        return Categories.objects.filter(client=self).order_by('-created_dt').first()
    
    class Meta:
        verbose_name_plural = 'Clients'



class Categories(models.Model):
    name=models.CharField(max_length=80,unique=True)
    item_number=models.IntegerField(validators=[MaxValueValidator(40),MinValueValidator(5)],default=12)
    client=models.ForeignKey(Clients,related_name='category',on_delete=models.CASCADE)
    created_dt=models.DateTimeField(auto_now_add=True)
    created_by=models.CharField(null=True,max_length=50)
    slug=models.SlugField(unique=True)
    

    
    def __str__(self):
        return self.name
    
    # def count_of_type(self):
    #     return Types.objects.filter(category=self).count()
    
    def save(self,*args, **kwargs ):
        self.slug=slugify(self.name)
        super().save(*args, **kwargs)

class List(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Categories,related_name='list',on_delete=models.CASCADE,null=True)
    count=models.CharField(max_length=3,null=True)
    time=models.CharField(max_length=4,null=True)
    num_motor=models.IntegerField(validators=[MaxValueValidator(12),MinValueValidator(3)],null=True)
    created_dt=models.DateTimeField(auto_now_add=True,null=True)
    updated_dt=models.DateTimeField(null=True)
    
    def __str__(self):
        return self.name
    
    def get_all_time(self):
        return self.time.all()