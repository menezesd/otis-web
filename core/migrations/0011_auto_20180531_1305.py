# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-31 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20180531_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='exam_family',
            field=models.CharField(choices=[('Waltz', 'Waltz'), ('Foxtrot', 'Foxtrot'), ('', '--')], default='', help_text='The family of practice exams to display.', max_length=10),
        ),
        migrations.AlterField(
            model_name='semester',
            name='active',
            field=models.BooleanField(default=False, help_text='Whether the semester is currently active (there should thus be at most one active semester).'),
        ),
    ]
