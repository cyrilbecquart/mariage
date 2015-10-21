# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mariage', '0003_auto_20151019_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='email',
            field=models.EmailField(max_length=100, null=True, verbose_name='email', blank=True),
        ),
    ]
