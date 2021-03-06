# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-04 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_ad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('img', models.CharField(db_index=True, max_length=200)),
                ('description', models.CharField(db_index=True, max_length=2000)),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренд',
                'ordering': ['name'],
            },
        ),
    ]
