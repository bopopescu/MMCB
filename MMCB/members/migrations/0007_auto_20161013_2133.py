# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 13:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20161002_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='accounts',
            field=models.CharField(help_text='範例：12345', max_length=5, validators=[django.core.validators.RegexValidator('^\\d{5}$', '請輸入匯款帳號後五碼', 'invalid')], verbose_name='匯款帳號後五碼'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='birthday',
            field=models.DateField(help_text='範例：1993/11/29', verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='phone',
            field=models.CharField(help_text='範例：0912456999', max_length=10, validators=[django.core.validators.RegexValidator('^09\\d{8}$', '請輸入正確的手機號碼', 'invalid')], verbose_name='手機'),
        ),
    ]
