# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-30 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0006_auto_20181130_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_result',
            name='api',
            field=models.CharField(max_length=32, verbose_name='功能接口'),
        ),
        migrations.AlterField(
            model_name='test_result',
            name='test_data',
            field=models.DateTimeField(auto_now=True, verbose_name='最后执行时间'),
        ),
    ]