# Generated by Django 3.2.8 on 2021-10-21 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0037_rename_last_announce_dismiss_userprofile_last_email_dismiss"),
        ("dashboard", "0062_auto_20211017_1819"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pset",
            name="next_unit_to_unlock",
            field=models.ForeignKey(
                blank=True,
                help_text="The unit you want to work on next (leave blank for none)",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="unblocking_psets",
                to="core.unit",
            ),
        ),
    ]
