# Generated by Django 2.2.6 on 2019-11-17 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug_product'),
        ),
    ]
