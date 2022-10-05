from multiprocessing import context
from unicodedata import category
from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import Products
import re
from category.models import Category,Subcategory
# Create your views here.
def adminproduct(request):
    name= request.user.username
    key1=Products.objects.all().order_by('id')
    context={'name':name,'key1':key1}
    return render(request,'adminproduct.html',context)

def addproduct(request):
    name= request.user.username
    categories=Category.objects.all()
    
    subcategories=Subcategory.objects.all()
    print(subcategories)
    context={'name':name,'categories':categories,'subcategories':subcategories}
    return render (request,'addproduct.html',context)

def addthisproduct(request):
    newproduct=Products()
    newproduct.product_name=request.POST.get('productname')
    newproduct.slug=request.POST.get('productname')

    newproduct.slug = newproduct.slug.lower().strip()
    newproduct.slug = re.sub(r'[^\w\s-]', '', newproduct.slug)
    newproduct.slug = re.sub(r'[\s_-]+', '-', newproduct.slug)
    newproduct.slug = re.sub(r'^-+|-+$', '', newproduct.slug)

    newproduct.price=request.POST.get('productprice')

    category_name=request.POST.get('categoryselected')
    
    category_nameused=Category.objects.get(id=category_name)
    newproduct.category_name=category_nameused
    newproduct.desciption=request.POST.get('productdescription')
    newproduct.stock=request.POST.get('stock')
    if int(newproduct.stock)>0:
        newproduct.is_available=True
    else:
        newproduct.is_available=False
    subcategory_name=request.POST.get('subcategoryselected')
    
    print(subcategory_name)
    if Subcategory.objects.get(id=subcategory_name):
        subcategory_nameused=Subcategory.objects.get(id=subcategory_name)
        newproduct.subcategory_name=subcategory_nameused
    
    if 'productimage' in request.FILES: 
        newproduct.images=request.FILES["productimage"]
    else :
        messages.info(request,"Require all fields")
        
    newproduct.save()    
    return redirect('adminproduct')

def deleteproduct(request,pk):
    get_data=Products.objects.get(id=pk)
    get_data.delete()
    return redirect('adminproduct')

def load_subcategory(request):
    category_id=request.GET.get('categoryselected')
    subcategories=Subcategory.objects.filter(category_id)