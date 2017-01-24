# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20170119_1515'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(related_name='order_items', default=1, to='shop.Profuct'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(related_name='items', to='orders.Order'),
        ),
    ]
