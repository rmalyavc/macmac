# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-18 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
