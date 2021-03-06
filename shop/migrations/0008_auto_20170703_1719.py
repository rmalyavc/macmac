# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-03 17:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_category_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('img', models.CharField(db_index=True, default=0, max_length=500)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Подкатегории',
                'verbose_name': 'Подкатегория',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.CharField(db_index=True, default=0, max_length=500),
        ),
        migrations.AddField(
            model_name='subcat',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subCats', to='shop.Category', verbose_name='Категория'),
        ),
    ]
