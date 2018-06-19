from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Brand(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    img = models.CharField(max_length=200, db_index=True)
    description = models.CharField(max_length=2000, db_index=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренд'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:BrandDetail', args=[self.id, self.slug])


class Ad(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    img = models.CharField(max_length=300, db_index=True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=1000, db_index=True)
    active = models.BooleanField(default=True, verbose_name="Активно")
    
    class Meta:
        ordering = ['created', 'updated']
        verbose_name = 'Объявление'
        verbose_name_plural = 'Обявления'
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:News', args=[self.slug])

    
# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    img = models.CharField(max_length=500, db_index=True, default=0)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.slug])
    
    def get_cat_url(self):
        return reverse('shop:SubCats', args=[self.slug])
    
    
class SubCat(models.Model):
    category = models.ForeignKey(Category, related_name='subCats', verbose_name="Категория", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    img = models.CharField(max_length=500, db_index=True, default=0)

    class Meta:
        ordering = ['name']
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.slug])   
        
        
# Модель продукта
class Product(models.Model):
    category = models.ForeignKey(SubCat, related_name='products', verbose_name="Категория", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    brand = models.CharField(max_length=200, db_index=True, verbose_name="Бренд")
    img = models.CharField(max_length=200, db_index=True, verbose_name="Фото")
    item_code = models.CharField(max_length=200, db_index=True, verbose_name="Артикул")
    discount = models.BooleanField(default=False, verbose_name="Акция")
    test_attr = models.CharField(max_length=200, verbose_name="Тест", default="test")

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="client")
    avatar = models.CharField(max_length=500, db_index=True)