# Generated by Django 2.0.6 on 2018-06-22 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20180622_1723'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proc',
            options={'ordering': ['name'], 'verbose_name': 'Процессор', 'verbose_name_plural': 'Процессоры'},
        ),
    ]