# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 07:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20160402_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 4, 3, 7, 23, 58, 311021, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 3, 15, 23, 34, 501734)),
        ),
    ]
