# Generated by Django 3.0.8 on 2020-07-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '', 'verbose_name_plural': ''},
        ),
        migrations.AlterField(
            model_name='product',
            name='availability',
            field=models.BooleanField(default=False, verbose_name='Есть в наличии'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity_purchases',
            field=models.IntegerField(default=0, verbose_name='Кол-во продаж'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
