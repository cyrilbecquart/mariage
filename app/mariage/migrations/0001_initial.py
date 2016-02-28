# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
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
                ('created_by', models.ForeignKey(related_name='hotels_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='hotels_modifier', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(verbose_name='created on', editable=False)),
                ('modified_date', models.DateTimeField(verbose_name='modified on', editable=False)),
                ('created_by', models.ForeignKey(related_name='userprofile_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='userprofile_modifier', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.OneToOneField(related_name='userprofile_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
