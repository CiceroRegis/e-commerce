# Generated by Django 2.2.6 on 2019-11-26 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20191126_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselimagehome',
            name='use',
            field=models.BooleanField(default=False),
        ),
    ]
