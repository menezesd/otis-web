# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 17:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("exams", "0005_auto_20170810_1230"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mockolympiad",
            old_name="solns_url",
            new_name="soln_url",
        ),
    ]
