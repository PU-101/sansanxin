# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20160407_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='visits',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
