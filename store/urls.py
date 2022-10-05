from . import views

from django.urls import path

urlpatterns = [
     path('',views.adminproduct,name="adminproduct"),
     path('addproduct',views.addproduct,name="addproduct"),
     path('addthisproduct',views.addthisproduct,name='addthisproduct'),
     path('load-subcategory/',views.load_subcategory,name="ajax_load_subcategory"),
     path('deleteproduct/<int:pk>',views.deleteproduct,name="deleteproduct")
]
