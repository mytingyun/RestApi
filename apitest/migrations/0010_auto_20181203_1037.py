# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-03 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0009_auto_20181201_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_manage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
            ],
        ),
        migrations.AlterField(
            model_name='test_result',
            name='test_data',
            field=models.DateTimeField(auto_now=True, verbose_name='最后执行时间'),
        ),
    ]
