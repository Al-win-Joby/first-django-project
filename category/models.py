from enum import unique
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name   =models.CharField(max_length=50)
    slug            =models.SlugField(max_length=100,unique=True)
    category_image  =models.ImageField(upload_to='photos/category',blank=True)
    description     =models.TextField(max_length=200,blank=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'
    
    def __str__(self):
        return self.category_name