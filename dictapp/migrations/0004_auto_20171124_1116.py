# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-24 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictapp', '0003_auto_20171124_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dict',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='dictapp/images/`upload_path`', width_field='width_field'),
        ),
    ]
