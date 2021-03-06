# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-28 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import system.storage


class Migration(migrations.Migration):

    dependencies = [
        ('apt', '0008_auto_20170726_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='cover',
            field=models.ImageField(blank=True, null=True, storage=system.storage.ImageStorage(), upload_to='cover/%Y/%m/%d/', verbose_name='活动封面'),
        ),
    ]
