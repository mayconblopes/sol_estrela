# Generated by Django 4.0.6 on 2022-07-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0006_product_in_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=False, editable=False, verbose_name='Em estoque'),
        ),
    ]