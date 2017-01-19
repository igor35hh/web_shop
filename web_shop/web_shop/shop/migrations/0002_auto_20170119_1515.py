# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profuct',
            name='available',
            field=models.BooleanField(default=True, verbose_name=b'Available'),
        ),
    ]
