from django.db import models

class Product(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название")

    description = models.TextField(
        null=True, blank=True, verbose_name="Описание")

    price = models.DecimalField(
        default=0,
        max_digits=11,
        decimal_places=2, 
        verbose_name="Цена")

    quantity_purchases = models.IntegerField(
        default=0, verbose_name="Кол-во продаж")

    availability = models.BooleanField(
        default=True, verbose_name="Есть в наличии")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Игры"
        verbose_name_plural = "игры"
