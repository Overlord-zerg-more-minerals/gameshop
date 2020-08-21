from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Название")

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание"
    )
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "категории"
    