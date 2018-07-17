# Generated by Django 2.0.6 on 2018-06-23 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_auto_20180622_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='test_attr',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='color', to='shop.Color', verbose_name='Цвет'),
            preserve_default=False,
        ),
    ]