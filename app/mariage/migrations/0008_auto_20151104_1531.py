# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mariage', '0007_auto_20151104_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpooling',
            name='places',
            field=models.IntegerField(blank=True, help_text='Number of places available or number of seats you or looking for.', null=True, verbose_name='places', validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='carpooling',
            name='role',
            field=models.CharField(default=b'DR', choices=[(b'DR', 'driver'), (b'PA', 'passenger')], max_length=2, help_text='Do you have a car or are you looking for one?', null=True, verbose_name='role'),
        ),
    ]
