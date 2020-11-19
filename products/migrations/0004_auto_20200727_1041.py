# Generated by Django 3.0.8 on 2020-07-27 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200726_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='display_image',
            field=models.URLField(default='#', verbose_name='display image'),
        ),
        migrations.AddField(
            model_name='product',
            name='fat_100g',
            field=models.SmallIntegerField(default=-1, verbose_name='Lipides'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_beverage',
            field=models.BooleanField(default=False, verbose_name='Boisson'),
        ),
        migrations.AddField(
            model_name='product',
            name='salt_100g',
            field=models.SmallIntegerField(default=-1, verbose_name='Sel'),
        ),
        migrations.AddField(
            model_name='product',
            name='satured_fat_100g',
            field=models.SmallIntegerField(default=-1, verbose_name='Acides gras'),
        ),
        migrations.AddField(
            model_name='product',
            name='small_image',
            field=models.URLField(default='#', verbose_name='small image'),
        ),
        migrations.AddField(
            model_name='product',
            name='sugars_100g',
            field=models.SmallIntegerField(default=-1, verbose_name='Sucres'),
        ),
        migrations.AddField(
            model_name='product',
            name='url_openfood',
            field=models.URLField(default='#', verbose_name='url product'),
        ),
    ]
