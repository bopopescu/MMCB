# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 16:47
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('sexual', models.CharField(choices=[('M', '男性'), ('F', '女性')], max_length=1, verbose_name='性別')),
                ('birthday', models.DateField(verbose_name='生日')),
                ('phone', models.CharField(help_text='範例：09XXXXXXXX', max_length=10, validators=[django.core.validators.RegexValidator('^09\\d{8}$', '請輸入正確的手機號碼', 'invalid')], verbose_name='手機')),
                ('email', models.EmailField(max_length=254)),
                ('accounts', models.CharField(help_text='範例：XXXXX', max_length=5, validators=[django.core.validators.RegexValidator('^\\d{5}$', '請輸入匯款帳號後五碼', 'invalid')], verbose_name='匯款帳號後五碼')),
                ('money', models.PositiveIntegerField(verbose_name='儲值金')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '會員資料',
                'ordering': ['id'],
                'verbose_name': '個資',
            },
        ),
    ]
