# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-08 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0003_auto_20171208_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication_bw',
            name='draftsman',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='작성자 이름'),
        ),
    ]
