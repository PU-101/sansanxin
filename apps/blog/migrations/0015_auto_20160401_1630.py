# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 08:30
from __future__ import unicode_literals

import apps.blog.models.upload_path
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20160330_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=apps.blog.models.upload_path.user_directory_path),
        ),
    ]