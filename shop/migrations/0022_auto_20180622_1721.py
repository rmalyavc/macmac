# Generated by Django 2.0.6 on 2018-06-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_ram'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterIndexTogether(
            name='proc',
            index_together={('id', 'slug')},
        ),
    ]
