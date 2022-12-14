from django.contrib import admin

from store.models import Products

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('product_name',)}
    list_display=('product_name','slug')
# Register your models here.
admin.site.register(Products,ProductAdmin)