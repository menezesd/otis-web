# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-31 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20180423_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitgroup',
            name='description',
            field=models.TextField(blank=True, help_text='A description of what this unit is'),
        ),
    ]
