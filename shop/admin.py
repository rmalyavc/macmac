from django.contrib import admin
from .models import Category, Product, Ad, Brand, SubCat, Client, Filt, Color, Memory, Unit, Ram, Proc, Diagonal, Material, Display

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

class FiltAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

class UnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

class MemoryAdmin(admin.ModelAdmin):
    list_display = ['val', 'unit']

class RamAdmin(admin.ModelAdmin):
    list_display = ['val', 'unit']

class ProcAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

class DiagonalAdmin(admin.ModelAdmin):
    list_display = ['val', 'unit']

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

class DisplayAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(SubCat, SubCatAdmin)
admin.site.register(Client)
admin.site.register(Filt, FiltAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Memory, MemoryAdmin)
admin.site.register(Ram, RamAdmin)
admin.site.register(Proc, ProcAdmin)
admin.site.register(Diagonal, DiagonalAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Display, DisplayAdmin)