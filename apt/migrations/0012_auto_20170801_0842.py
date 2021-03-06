# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-01 08:42
from __future__ import unicode_literals

from django.db import migrations, models
import system.storage


class Migration(migrations.Migration):

    dependencies = [
        ('apt', '0011_auto_20170731_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='plane_graph1',
            field=models.ImageField(blank=True, null=True, storage=system.storage.ImageStorage(), upload_to='planeGraph1/%Y/%m/%d/', verbose_name='平面图1'),
        ),
        migrations.AddField(
            model_name='event',
            name='plane_graph2',
            field=models.ImageField(blank=True, null=True, storage=system.storage.ImageStorage(), upload_to='planeGraph2/%Y/%m/%d/', verbose_name='平面图2'),
        ),
    ]
