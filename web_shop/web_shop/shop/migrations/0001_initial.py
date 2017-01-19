# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Profuct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Title', db_index=True)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(upload_to=b'products/%Y/%m/%d/', verbose_name=b'Product picture', blank=True)),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
                ('price', models.DecimalField(verbose_name=b'Price', max_digits=10, decimal_places=2)),
                ('stock', models.PositiveIntegerField(verbose_name=b'In of stock')),
                ('available', models.BinaryField(default=True, verbose_name=b'Available')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(related_name='products', verbose_name=b'Category', to='shop.Category')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterIndexTogether(
            name='profuct',
            index_together=set([('id', 'slug')]),
        ),
    ]
