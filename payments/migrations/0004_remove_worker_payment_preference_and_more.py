# Generated by Django 4.0.8 on 2022-12-02 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_alter_calendar_urls_again'),
        ('payments', '0003_alter_worker_notes_alter_worker_paypal_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='payment_preference',
        ),
        migrations.AddField(
            model_name='job',
            name='payment_preference',
            field=models.CharField(choices=[('', 'Not specified'), ('INV', 'Invoice adjustment'), ('PB', 'Pro bono'), ('PPL', 'PayPal'), ('VNM', 'Venmo'), ('ZLL', 'Zelle')], default='', max_length=3),
        ),
        migrations.AddField(
            model_name='jobfolder',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.semester'),
        ),
    ]
