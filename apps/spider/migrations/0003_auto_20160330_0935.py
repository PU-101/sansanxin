# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0002_auto_20160329_1428'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mafengwomodel',
            options={},
        ),
        migrations.RenameField(
            model_name='mafengwomodel',
            old_name='image_src',
            new_name='picture',
        ),
        migrations.AddField(
            model_name='mafengwomodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
