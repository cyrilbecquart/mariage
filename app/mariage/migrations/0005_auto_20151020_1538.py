# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariage', '0004_auto_20151020_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='latitude',
            field=models.FloatField(null=True, verbose_name='latitude', blank=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='longitude',
            field=models.FloatField(null=True, verbose_name='longitude', blank=True),
        ),
    ]
