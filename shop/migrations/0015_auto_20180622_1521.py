# Generated by Django 2.0.6 on 2018-06-22 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20180621_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
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
            model_name='filt',
            name='cats',
            field=models.ManyToManyField(related_name='filt_cats', to='shop.Category', verbose_name='Категории'),
        ),
        migrations.AddField(
            model_name='color',
            name='filt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='shop.Filt', verbose_name='Цвета'),
        ),
        migrations.AlterIndexTogether(
            name='color',
            index_together={('id', 'slug')},
        ),
    ]