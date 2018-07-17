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

    def get_fake_url(self):
        return reverse('shop:FakeListByCategory', args=[self.slug])
    
    
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

    # def get_fake_url(self):
    #     return reverse('shop:FakeList', args=[self.slug])

class Unit(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    verb = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name
      
class Color(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    verb = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

class Memory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    unit = models.ForeignKey(Unit, related_name='mem_sizes', verbose_name="Единицы", on_delete=models.CASCADE)
    val = models.PositiveIntegerField(verbose_name="Объём")

    class Meta:
        ordering = ['val']
        verbose_name = 'Память'
        verbose_name_plural = 'Память'

    def __str__(self):
        return self.name

class Ram(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    unit = models.ForeignKey(Unit, related_name='ram_sizes', verbose_name="Объём оперативной памяти", on_delete=models.CASCADE)
    val = models.PositiveIntegerField(verbose_name="Объём")

    class Meta:
        ordering = ['val']
        verbose_name = 'Оперативная память'
        verbose_name_plural = 'Оперативная память'

    def __str__(self):
        return self.name

class Diagonal(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    unit = models.ForeignKey(Unit, related_name='diagonal', verbose_name="Диагональ экрана", on_delete=models.CASCADE)
    val = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Диагональ экрана")

    class Meta:
        ordering = ['val']
        verbose_name = 'Диагональ экрана'
        verbose_name_plural = 'Диагонали экрана'

    def __str__(self):
        return self.name

class Proc(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

class Display(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    verb = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Тип дисплея'
        verbose_name_plural = 'Типы дисплея'
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    verb = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

# Модель продукта
class Product(models.Model):
    category = models.ForeignKey(SubCat, related_name='products', verbose_name="Категория", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to="polls/static/shop/products/%Y/%m/%d/", blank=True, verbose_name="Изображение товара")
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
    color = models.ForeignKey(Color, related_name='color', verbose_name="Цвет", on_delete=models.CASCADE)
    memory = models.ForeignKey(Memory, related_name='memory', verbose_name="Память", default=0, on_delete=models.CASCADE)
    ram = models.ForeignKey(Ram, related_name='ram', verbose_name="Оперативная память", default=0, on_delete=models.CASCADE)
    diagonal = models.ForeignKey(Diagonal, related_name='diagonal', verbose_name="Диагональ экрана", default=0, on_delete=models.CASCADE)
    proc = models.ForeignKey(Proc, related_name='proc', verbose_name="Процессор", default=0, on_delete=models.CASCADE)
    display = models.ForeignKey(Display, related_name='display', verbose_name="Дисплей", default=0, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, related_name='material', verbose_name="Материал", default=0, on_delete=models.CASCADE)
    refer_to = models.ManyToManyField(SubCat, related_name='refer_to', verbose_name="Совместимость")
    url = models.CharField(max_length=200, db_index=True, default=0)
    # test_attr = models.CharField(max_length=200, verbose_name="Тест", default="test")

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

class Filt(models.Model):
    cats = models.ManyToManyField(Category, related_name='filt_cats', verbose_name="Категории")
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

# class Filt(models.Model):
#     bs = models.ManyToManyField(Category, null=True, blank=True, related_query_name='filt_cats', db_table='A_B_relation')
#     name = models.CharField(max_length=50,unique=True)

#     def __str__(self):              # __unicode__ on Python 
#         return self.name

# class Category(models.Model):
#     url = models.URLField(null=True, blank=True)
#     name = models.CharField(max_length=50,unique=True)

#     def __str__(self):              # __unicode__ on Python 
#         return self.name

# You can retrieve a list of Filt objects that are related to a specific Category object:

# cat_object = Category.objects.get(name='Mac')
# Filt.objects.filter(bs=b_object)


# If you want a list of Category objects

# b_object_list = Category.objects.filter(name__in=['Bob', 'Jim'])
# Filt.objects.filter(bs__in=b_object_list)