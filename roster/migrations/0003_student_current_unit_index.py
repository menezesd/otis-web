# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-06 00:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roster", "0002_auto_20170806_0016"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="current_unit_index",
            field=models.IntegerField(
                default=0,
                help_text="If this is equal to k, then the student has completed the first k units of his/her curriculum and is working on the (k+1)st unit",
            ),
        ),
    ]
