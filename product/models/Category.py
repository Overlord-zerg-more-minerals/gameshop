from django.db import models


class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание"
    )
    
    parent_category = models.ForeignKey(
        to="Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="child_category"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "категории"
    