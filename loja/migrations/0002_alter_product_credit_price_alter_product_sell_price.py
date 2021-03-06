# Generated by Django 4.0.6 on 2022-07-10 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='credit_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço a prazo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sell_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço de venda'),
        ),
    ]
