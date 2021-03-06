# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160315_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='followers',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='follows',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
