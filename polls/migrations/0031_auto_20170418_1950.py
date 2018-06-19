# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-18 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0030_auto_20170418_1943'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=2, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
