# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-21 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20180221_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='price_trend',
            field=models.IntegerField(default=0),
        ),
    ]
