# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mariage', '0005_auto_20151020_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carpooling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created on', editable=False)),
                ('modified_date', models.DateTimeField(verbose_name='modified on', editable=False)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='email', blank=True)),
                ('phone', models.CharField(max_length=100, null=True, verbose_name='phone', blank=True)),
                ('role', models.CharField(default=b'DR', choices=[(b'DR', 'driver'), (b'PA', 'passenger')], max_length=2, blank=True, null=True, verbose_name='role')),
                ('places', models.IntegerField(null=True, verbose_name='website', blank=True)),
                ('departure', models.CharField(max_length=100, null=True, verbose_name='departure town', blank=True)),
                ('created_by', models.ForeignKey(related_name='carpooling_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='carpooling_modifier', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
