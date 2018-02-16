# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-16 12:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20180211_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='price_trend',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='time_of_post',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 2, 16, 18, 10, 25, 128612)),
        ),
    ]
