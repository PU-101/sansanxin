# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 08:52
from __future__ import unicode_literals

import apps.users.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(choices=[('M', '男生'), ('F', '女生')], default='F', max_length=1)),
                ('birthday', models.DateField()),
                ('signature', models.CharField(default='什么都没留下', max_length=40)),
                ('portrait', models.ImageField(default=apps.users.models.default_portrait, upload_to=apps.users.models.user_directory_path)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
