# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20170119_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('last_name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('address', models.CharField(max_length=250, verbose_name=b'Adrress')),
                ('postal_code', models.CharField(max_length=20, verbose_name=b'Postal code')),
                ('city', models.CharField(max_length=100, verbose_name=b'City')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'Updated')),
                ('paid', models.BooleanField(default=False, verbose_name=b'Paid')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(verbose_name=b'Price', max_digits=10, decimal_places=2)),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name=b'Quantity')),
                ('order', models.ForeignKey(related_name='order_items', to='shop.Profuct')),
            ],
        ),
    ]
