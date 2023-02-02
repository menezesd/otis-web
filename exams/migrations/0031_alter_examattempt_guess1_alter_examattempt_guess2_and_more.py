# Generated by Django 4.0.8 on 2022-11-06 01:16

from django.db import migrations, models

import exams.models


class Migration(migrations.Migration):

    dependencies = [
        ("exams", "0030_alter_mockcompleted_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="examattempt",
            name="guess1",
            field=models.CharField(
                blank=True,
                max_length=128,
                validators=[exams.models.expr_validator],
                verbose_name="Problem 1 response",
            ),
        ),
        migrations.AlterField(
            model_name="examattempt",
            name="guess2",
            field=models.CharField(
                blank=True,
                max_length=128,
                validators=[exams.models.expr_validator],
                verbose_name="Problem 2 response",
            ),
        ),
        migrations.AlterField(
            model_name="examattempt",
            name="guess3",
            field=models.CharField(
                blank=True,
                max_length=128,
                validators=[exams.models.expr_validator],
                verbose_name="Problem 3 response",
            ),
        ),
        migrations.AlterField(
            model_name="examattempt",
            name="guess4",
            field=models.CharField(
                blank=True,
                max_length=128,
                validators=[exams.models.expr_validator],
                verbose_name="Problem 4 response",
            ),
        ),
        migrations.AlterField(
            model_name="examattempt",
            name="guess5",
            field=models.CharField(
                blank=True,
                max_length=128,
                validators=[exams.models.expr_validator],
                verbose_name="Problem 5 response",
            ),
        ),
        migrations.AlterField(
            model_name="practiceexam",
            name="answer1",
            field=models.CharField(
                blank=True,
                max_length=128,
                validators=[exams.models.expr_validator_multiple],
            ),
        ),
        migrations.AlterField(
            model_name="practiceexam",
            name="answer2",
            field=models.CharField(
                blank=True,
                max_length=128,
                validators=[exams.models.expr_validator_multiple],
            ),
        ),
        migrations.AlterField(
            model_name="practiceexam",
            name="answer3",
            field=models.CharField(
                blank=True,
                max_length=128,
                validators=[exams.models.expr_validator_multiple],
            ),
        ),
        migrations.AlterField(
            model_name="practiceexam",
            name="answer4",
            field=models.CharField(
                blank=True,
                max_length=128,
                validators=[exams.models.expr_validator_multiple],
            ),
        ),
        migrations.AlterField(
            model_name="practiceexam",
            name="answer5",
            field=models.CharField(
                blank=True,
                max_length=128,
                validators=[exams.models.expr_validator_multiple],
            ),
        ),
    ]
