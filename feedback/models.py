from django.db import models
from django.contrib.auth.models import User


# class Feedback(models.Model):
#     name = models.CharField(
#         max_length=255,
#         null=True,
#         blank=True,
#         verbose_name="Ваше имя"
#     )

#     text = models.TextField(
#         null=True,
#         blank=True,
#         verbose_name="Текст обращения"
#     )

#     screen = models.ImageField(
#         upload_to="feedback_image",
#         null=True,
#         blank=True,
#         verbose_name="Изображение"
#     )

#     user = models.ForeignKey(
#         to=User,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True
#     )

#     date = models.DateTimeField(
#         auto_now_add=True
#     ) 

#     phone = models.IntegerField(
#         max_length=255,
#         null=True,
#         blank=True,
#         verbose_name="Номер телефона"
#     )

#     email = models.EmailField(
#         max_length=255,
#         null=True,
#         blank=True,
#         verbose_name="Email"
#     )

#     class Meta:
#         verbose_name = "Обратная связь"
#         verbose_name_plural = "Формы обратной связи"
