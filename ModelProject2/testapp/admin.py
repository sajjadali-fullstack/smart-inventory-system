from django.contrib import admin
from testapp.models import  Products


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_id','product_name','price','insurance','mfg']
    
admin.site.register(Products, ProductsAdmin)