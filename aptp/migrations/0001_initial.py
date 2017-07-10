# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-10 00:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apt', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='顾客名')),
                ('eventdetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apt.EventDetail', verbose_name='房源/车位信息')),
            ],
        ),
    ]
