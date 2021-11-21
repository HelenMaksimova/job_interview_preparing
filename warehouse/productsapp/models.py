from django.db import models
from datetime import date


class Vendor(models.Model):
    """
    Модель поставщика
    """
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Модель продукта
    """

    PIECE = 'PC'
    KILOGRAM = 'KG'
    GRAM = 'GM'
    LITER = 'LR'
    MILLILITER = 'ML'
    PACK = 'PK'

    UNIT_CHOICES = [
        (PIECE, 'шт'),
        (KILOGRAM, 'кг'),
        (GRAM, 'г'),
        (LITER, 'л'),
        (MILLILITER, 'мл'),
        (PACK, 'уп'),
    ]

    name = models.CharField(max_length=255, verbose_name='название')
    received_date = models.DateField(default=date.today, verbose_name='дата поступления')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name='цена')
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default=PIECE, verbose_name='ед. измерения')
    vendor_name = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True,
                                    verbose_name='поставщик', related_name='products')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
