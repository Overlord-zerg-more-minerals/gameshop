# Generated by Django 3.0.8 on 2020-07-28 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='static/no_image.png', null=True, upload_to='game_images', verbose_name='Изображение Игры'),
        ),
    ]
