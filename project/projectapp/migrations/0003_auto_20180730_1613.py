# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-30 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_studentenroll_useremail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_name',
            field=models.CharField(blank=True, default=b'', max_length=30),
        ),
    ]
