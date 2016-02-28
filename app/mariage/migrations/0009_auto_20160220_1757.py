# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mariage', '0008_auto_20151104_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created on', editable=False)),
                ('modified_date', models.DateTimeField(verbose_name='modified on', editable=False)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('when', models.CharField(max_length=100, null=True, verbose_name='When')),
                ('order', models.IntegerField(blank=True, help_text='Order during ceremony.', null=True, verbose_name='Order', validators=[django.core.validators.MinValueValidator(1)])),
                ('partition', models.FileField(upload_to=b'songs', verbose_name='Music sheet', blank=True)),
                ('four_voice', models.FileField(upload_to=b'songs', verbose_name='4 voices', blank=True)),
                ('soprane', models.FileField(upload_to=b'songs', verbose_name='soprane', blank=True)),
                ('alto', models.FileField(upload_to=b'songs', verbose_name='alto', blank=True)),
                ('tenor', models.FileField(upload_to=b'songs', verbose_name='tenor', blank=True)),
                ('basse', models.FileField(upload_to=b'songs', verbose_name='basse', blank=True)),
                ('created_by', models.ForeignKey(related_name='song_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='song_modifier', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='carpooling',
            name='places',
            field=models.IntegerField(blank=True, help_text='Number of places available or number of seats you are looking for.', null=True, verbose_name='places', validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(1)]),
        ),
    ]
