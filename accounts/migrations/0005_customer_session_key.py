# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-03 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_expire_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='session_key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
