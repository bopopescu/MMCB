# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-13 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_auto_20161010_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='date_remittance',
            field=models.DateTimeField(blank=True, null=True, verbose_name='匯款日期時間'),
        ),
    ]