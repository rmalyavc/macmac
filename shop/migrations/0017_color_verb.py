# Generated by Django 2.0.6 on 2018-06-22 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_remove_color_filt'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='verb',
            field=models.CharField(db_index=True, default=0, max_length=200),
            preserve_default=False,
        ),
    ]