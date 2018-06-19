from django.contrib import admin
from .models import Category, Product, Ad, Brand, SubCat, Client

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name', )}

class AdAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'created', 'updated', 'active']
    list_filter = ['created', 'updated']
    prepopulated_fields = {'slug': ('name', )}


class SubCatAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
    
# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
# Модель товара

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(SubCat, SubCatAdmin)
admin.site.register(Client)