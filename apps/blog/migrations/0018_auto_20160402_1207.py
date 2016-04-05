# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20160401_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments_num',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes_num',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='views_num',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='followers_num',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='follows_num',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='posts_num',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
