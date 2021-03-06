# Generated by Django 2.2.6 on 2019-11-26 22:35

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_delete_carouselimagehome'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImageHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carouselImage', filebrowser.fields.FileBrowseField(max_length=200, null=True, verbose_name='carouselImage')),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('use', models.BooleanField(default=False)),
            ],
        ),
    ]
