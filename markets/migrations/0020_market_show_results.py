# Generated by Django 5.1.7 on 2025-03-22 09:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("markets", "0019_market_int_guesses_only"),
    ]

    operations = [
        migrations.AddField(
            model_name="market",
            name="show_results",
            field=models.BooleanField(default=True),
        ),
    ]
