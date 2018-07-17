# Generated by Django 2.0.6 on 2018-06-21 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20180621_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filt',
            name='category',
        ),
        migrations.AddField(
            model_name='filt',
            name='category',
            field=models.ManyToManyField(related_name='filters', to='shop.Category', verbose_name='Категории'),
        ),
    ]
