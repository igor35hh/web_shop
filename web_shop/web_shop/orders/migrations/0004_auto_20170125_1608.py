# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cupons', '0001_initial'),
        ('orders', '0003_auto_20170125_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cupon',
            field=models.ForeignKey(related_name='orders', blank=True, to='cupons.Cupon', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
