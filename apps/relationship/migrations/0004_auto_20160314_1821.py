# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship', '0003_auto_20160314_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='situation',
            field=models.IntegerField(default=10),
        ),
    ]
