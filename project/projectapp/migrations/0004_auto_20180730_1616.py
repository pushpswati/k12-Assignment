# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-30 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0003_auto_20180730_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentenroll',
            name='password',
            field=models.CharField(blank=True, default=b'', max_length=10),
        ),
    ]
