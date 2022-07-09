from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('MENINO', 'Menino'),
        ('MENINA', 'Menina'),
    ]

    SIZE_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('P', 'P'),
        ('M', 'M'),
        ('G', 'G'),
    ]

    img = models.ImageField(upload_to='static/product_photos', verbose_name='Foto')
    description = models.CharField(max_length=1000, verbose_name='Descrição')
    aquisition_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço de aquisição')
    aquisition_data = models.DateField(verbose_name='Data de aquisição')
    sell_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço de venda")
    genre = models.CharField(max_length=6, choices=CATEGORY_CHOICES, verbose_name="Gênero")
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, verbose_name="Tamanho")
    quantity = models.PositiveIntegerField(verbose_name='Quantidade em estoque')

    class Meta:
        verbose_name = 'Produto'
        ordering = ('-aquisition_data',)

    def __str__(self):
        return self.description[:255]
