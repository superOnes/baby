# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-26 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apt', '0006_event_house_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetail',
            name='status',
            field=models.BooleanField(default=True, verbose_name='上架状态'),
        ),
    ]
