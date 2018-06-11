# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-05 01:28
from __future__ import unicode_literals

import dictapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictapp', '0007_auto_20171130_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dict',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to=dictapp.models.upload_path_audio, verbose_name='티벳어 발음 오디오'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='bu_classification',
            field=models.CharField(choices=[('《경장》', '《경장》'), ('《율장》', '《율장》'), ('《논장》', '《논장》'), ('《주석》', '《주석》'), ('《찬가》', '《찬가》'), ('《서신》', '《서신》'), ('《시문》', '《시문》'), ('《역사》', '《역사》'), ('《우화》', '《우화》'), ('《인명》', '《인명》'), ('《지명》', '《지명》'), ('《의례》', '《의례》'), ('《복식》', '《복식》'), ('《사원》', '《사원》')], default='FR', max_length=10, verbose_name='불교 단어 분류'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='classification',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2, verbose_name='단어 분류'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=dictapp.models.upload_path_file, verbose_name='파일'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=dictapp.models.upload_path_img, verbose_name='사진자료', width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='단어설명'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='ti_antonym',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='반의어'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='ti_classical_chinese_entry',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='한문'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='ti_english_entry',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='영어'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='ti_future_tense',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='동사-미래형'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='ti_honorific',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='높임말'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='ti_humble_terms',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='낮춤말'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='ti_imperative',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='동사-명령형'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='ti_korean_entry',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='한국어 표제어'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='ti_pali_entry',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='빨리어'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='ti_past_tense',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='동사-과거형'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='ti_present_tense',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='동사-현재형'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='ti_sanskrit_entry',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='산스끄리뜨'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='ti_synonym',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='동의어'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='ti_thesaurus',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='유의어'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='ti_wylie',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='티벳어 와일리표기'),
        ),
        migrations.AlterField(
            model_name='dict',
            name='title',
            field=models.CharField(max_length=200, verbose_name='티벳어 표제어'),
        ),
    ]
