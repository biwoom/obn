# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-24 02:38
from __future__ import unicode_literals

import dictapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictapp', '0005_auto_20171124_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='dict',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to=dictapp.models.upload_path_audio),
        ),
    ]