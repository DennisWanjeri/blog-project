# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2022-07-26 22:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220726_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='create_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 26, 22, 17, 37, 189880, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 26, 22, 17, 37, 189880, tzinfo=utc)),
        ),
    ]
