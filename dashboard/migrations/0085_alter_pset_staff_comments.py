# Generated by Django 4.1.7 on 2023-03-07 23:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0084_rename_comments_pset_staff_comments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pset",
            name="staff_comments",
            field=models.TextField(
                blank=True, help_text="Comments by Evan on this problem set"
            ),
        ),
    ]