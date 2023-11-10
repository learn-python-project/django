from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock", "image_url", "category")
    
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    
admin.site.register(Category, CategoryAdmin)