# Generated by Django 3.0.8 on 2020-07-26 14:30

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id_category', models.CharField(max_length=150, primary_key=True, serialize=False, verbose_name='id_category')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='id_category', unique=True, verbose_name='id Category Adress')),
                ('name', models.CharField(max_length=255, verbose_name='url catégorie')),
                ('products', models.IntegerField(verbose_name='Nb produits')),
                ('url', models.CharField(max_length=255, verbose_name='url catégorie')),
                ('visible', models.BooleanField(verbose_name='visible')),
            ],
        ),
        migrations.CreateModel(
            name='CatProd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_product', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='id_product')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='id_product', unique=True, verbose_name='id Product Address')),
                ('product_name_fr', models.CharField(max_length=150, verbose_name='nom produit')),
                ('nutriscore_score', models.IntegerField(verbose_name='score produit')),
                ('nutriscore_grade', models.CharField(choices=[('A', 'Score A'), ('B', 'Score B'), ('C', 'Score C'), ('D', 'Score D'), ('E', 'Score E')], max_length=1, verbose_name='grade produit')),
                ('stores', models.CharField(max_length=255, verbose_name='magasins')),
                ('generic_name_fr', models.TextField(blank=True, verbose_name='description')),
                ('brands', models.CharField(max_length=100, verbose_name='marque')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
