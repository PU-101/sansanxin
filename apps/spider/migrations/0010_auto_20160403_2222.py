# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 14:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0009_auto_20160402_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calendar',
            old_name='destinaion',
            new_name='destination',
        ),
    ]
