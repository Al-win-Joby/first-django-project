
from django.db import models

from category.models import Category, Subcategory

# Create your models here.
class Products(models.Model):
    product_name    =models.CharField(max_length=200,unique=True)
    slug            =models.SlugField(max_length=200,unique=True)
    desciption      =models.TextField(max_length=200,blank=True)
    price           =models.IntegerField()
    images          =models.ImageField(upload_to='photos/store')
    stock           =models.IntegerField()
    is_available    =models.BooleanField(default=True)
    category_name        =models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory_name    =models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    
    created_date    =models.DateTimeField(auto_now_add=True)
    modified_date   =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name