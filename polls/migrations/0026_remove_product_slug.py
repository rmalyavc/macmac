# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-18 19:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_auto_20170418_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
