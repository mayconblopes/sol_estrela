from django.db import models
from multiselectfield import MultiSelectField


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
    credit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço a prazo")
    genre = models.CharField(max_length=6, choices=CATEGORY_CHOICES, verbose_name="Gênero")
    size = MultiSelectField(choices=SIZE_CHOICES, verbose_name="Tamanho", blank=True)
    in_stock = models.BooleanField(verbose_name='Em estoque', default=False, editable=False)

    class Meta:
        verbose_name = 'Produto'
        ordering = ('-aquisition_data',)

    def __str__(self):
        return self.description[:255]

    def save(self, *args, **kwargs):
        """overrides save method to change in_stock attribute"""
        if len(self.size):
            self.in_stock = True
        else:
            self.in_stock = False

        return super().save(*args, **kwargs)
