# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-08 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20170703_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='test_attr',
            field=models.CharField(default='test', max_length=200, verbose_name='Тест'),
        ),
    ]
