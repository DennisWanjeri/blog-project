# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2022-07-26 21:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 26, 21, 53, 44, 702780, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 26, 21, 53, 44, 702780, tzinfo=utc)),
        ),
    ]
