# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-20 03:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apt', '0004_eventdetail_sign'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventdetail',
            name='price',
        ),
    ]
