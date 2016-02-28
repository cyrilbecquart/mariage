# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariage', '0002_auto_20151017_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='email',
            field=models.EmailField(max_length=100, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='description',
            field=models.CharField(max_length=2048, null=True, verbose_name='description', blank=True),
        ),
    ]
