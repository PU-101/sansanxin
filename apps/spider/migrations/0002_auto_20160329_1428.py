# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mafengwomodel',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='mafengwomodel',
            name='image_src',
            field=models.URLField(null=True),
        ),
    ]
