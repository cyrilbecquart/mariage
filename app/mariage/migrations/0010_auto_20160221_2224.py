# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mariage', '0009_auto_20160220_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='order',
            field=models.IntegerField(blank=True, help_text='Order in page', null=True, verbose_name='Order', validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='carpooling',
            name='role',
            field=models.CharField(default=b'DR', choices=[(b'DR', 'Driver'), (b'PA', 'Passenger')], max_length=2, help_text='Do you have a car or are you looking for one?', null=True, verbose_name='role'),
        ),
    ]
