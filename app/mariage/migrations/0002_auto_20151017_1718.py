# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mariage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created on', editable=False)),
                ('modified_date', models.DateTimeField(verbose_name='modified on', editable=False)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('phone', models.CharField(max_length=100, null=True, verbose_name='phone', blank=True)),
                ('description', models.CharField(max_length=1024, null=True, verbose_name='description', blank=True)),
                ('website', models.URLField(max_length=1024, null=True, verbose_name='website', blank=True)),
                ('price_range', models.CharField(max_length=100, null=True, verbose_name='price range', blank=True)),
                ('address', models.CharField(max_length=1024, null=True, verbose_name='address', blank=True)),
                ('created_by', models.ForeignKey(related_name='hotel_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='hotel_modifier', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='hotels',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='hotels',
            name='modified_by',
        ),
        migrations.DeleteModel(
            name='Hotels',
        ),
    ]
