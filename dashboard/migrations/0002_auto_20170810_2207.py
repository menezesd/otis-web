# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 03:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="uploadedfile",
            old_name="content",
            new_name="file_content",
        ),
    ]
