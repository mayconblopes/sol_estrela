# Generated by Django 4.0.6 on 2022-07-09 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='static/product_photos', verbose_name='Foto'),
        ),
    ]
