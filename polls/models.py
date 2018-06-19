import datetime

from django.db import models
from django.utils import timezone

class Product(models.Model):
    item_code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    madeIn = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        return self.item_code
        return self.price
        return self.image
        return self.description
        return self.madeIn
        return self.category
        # return self.brand
        

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
        return self.image
        
class Brands(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
        return self.image
        return self.image
        
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text