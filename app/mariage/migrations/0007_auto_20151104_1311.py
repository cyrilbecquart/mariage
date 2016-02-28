# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mariage', '0006_carpooling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpooling',
            name='places',
            field=models.IntegerField(blank=True, null=True, verbose_name='website', validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(1)]),
        ),
    ]
