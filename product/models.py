from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название")

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="product",
        verbose_name="Продавец"
    )

    category = models.ForeignKey(
        to="Category",
        on_delete=models.SET_NULL,
        related_name="product",
        null=True,
        blank=True,
        verbose_name="Категория"
    )

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="game_images",
        verbose_name="Изображение Игры",
        default="static/no_image.png"
    )

    description = models.TextField(
        null=True, blank=True, verbose_name="Описание")

    price = models.DecimalField(
        default=0,
        max_digits=11,
        decimal_places=2, 
        verbose_name="Цена"
    )

    quantity_purchases = models.IntegerField(
        default=0, verbose_name="Кол-во продаж")

    availability = models.BooleanField(
        default=True, verbose_name="Есть в наличии")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Игру"
        verbose_name_plural = "Игры"


class Category(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "категории"
    


