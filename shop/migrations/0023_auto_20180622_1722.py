# Generated by Django 2.0.6 on 2018-06-22 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_auto_20180622_1721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proc',
            options={'ordering': ['name'], 'verbose_name': 'Процессор'},
        ),
    ]