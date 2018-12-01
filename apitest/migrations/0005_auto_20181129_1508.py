# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-29 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0004_auto_20181129_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='start_test',
            name='api',
            field=models.ManyToManyField(to='apitest.ApiManage', verbose_name='运行的接口'),
        ),
        migrations.AlterField(
            model_name='apimanage',
            name='apiname',
            field=models.CharField(max_length=32, unique=True, verbose_name='接口功能'),
        ),
    ]
