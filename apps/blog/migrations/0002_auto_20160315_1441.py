# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 06:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='star',
            name='by',
        ),
        migrations.RemoveField(
            model_name='star',
            name='to',
        ),
        migrations.RemoveField(
            model_name='post',
            name='stars',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Star',
        ),
    ]