# Generated by Django 4.0.6 on 2022-07-10 12:51

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(0, 'SEM ESTOQUE'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('P', 'P'), ('M', 'M'), ('G', 'G')], max_length=48, verbose_name='Tamanho'),
        ),
    ]
