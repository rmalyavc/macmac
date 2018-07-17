# Generated by Django 2.0.6 on 2018-06-22 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_memory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='memory',
            name='val',
            field=models.PositiveIntegerField(verbose_name='Объём'),
        ),
        migrations.AlterIndexTogether(
            name='unit',
            index_together={('id', 'slug')},
        ),
        migrations.AddField(
            model_name='memory',
            name='unit',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='mem_sizes', to='shop.Unit', verbose_name='Единицы'),
            preserve_default=False,
        ),
    ]
