# Generated by Django 2.0.6 on 2018-06-23 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_auto_20180623_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/media/products/%Y/%m/%d/', verbose_name='Изображение товара'),
        ),
    ]