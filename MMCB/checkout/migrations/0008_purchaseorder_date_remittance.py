# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-02 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20160929_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='date_remittance',
            field=models.DateField(blank=True, null=True, verbose_name='匯款日期'),
        ),
    ]