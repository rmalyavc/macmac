# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-18 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_auto_20170418_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]