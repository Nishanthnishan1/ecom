from typing import Iterable, Optional
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.views import LoginView


# Create your models here.
class categ(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    
    

    class Meta:
        ordering=('name',)
        verbose_name='categories'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])
    
    def __str__(self):
        return '{}'.format(self.name)





class products(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to='products')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)


    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])
    
    
    def __str__(self):
        return '{}'.format(self.name)
    


class UserProfile(models.Model):
    Uname=models.CharField(max_length=100)
    address=models.CharField(max_length=250)
    contact=models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128) 
    
    
    def __str__(self):
        return self.Uname
    




    




class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    def __self__(self):
        return self.username