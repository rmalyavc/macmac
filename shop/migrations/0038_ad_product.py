# Generated by Django 2.0.7 on 2018-07-17 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0037_auto_20180717_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='product',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='shop.Product', verbose_name='Товар'),
        ),
    ]