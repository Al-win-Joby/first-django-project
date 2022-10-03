from cgi import print_exception
from email.policy import default
from enum import unique
from operator import truediv
from unicodedata import category
from django.db import models

from category.models import Category

# Create your models here.
class Products(models.Model):
    product_name    =models.CharField(max_length=200,unique=True)
    slug            =models.SlugField(max_length=200,unique=True)
    desciption      =models.TextField(max_length=200,blank=True)
    price           =models.IntegerField()
    images          =models.ImageField(upload_to='photos/store')
    stock           =models.IntegerField()
    is_available    =models.BooleanField(default=True)
    category        =models.ForeignKey(Category,on_delete=models.CASCADE)
    
    created_date    =models.DateTimeField(auto_now_add=True)
    modified_date   =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name