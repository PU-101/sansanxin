# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 13:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160317_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='comments',
            new_name='comments_num',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='likes_hum',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='views',
            new_name='views_num',
        ),
    ]