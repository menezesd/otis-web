# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 04:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("exams", "0009_assignment_start_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="assignment",
            options={"ordering": ("due_date", "start_date", "name")},
        ),
        migrations.AlterModelOptions(
            name="mockolympiad",
            options={"ordering": ("due_date", "start_date", "family", "number")},
        ),
    ]
