# Generated by Django 3.2.7 on 2021-09-17 00:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0075_remove_student_last_level_time'),
        ('dashboard', '0047_bonuslevel_bonuslevelunlock'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='creator',
            field=models.ForeignKey(blank=True, help_text='Student who owns this achievement', null=True, on_delete=django.db.models.deletion.CASCADE, to='roster.student'),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='code',
            field=models.CharField(blank=True, max_length=96, null=True, unique=True, validators=[django.core.validators.RegexValidator(regex='[a-f0-9]{24}')]),
        ),
        migrations.CreateModel(
            name='PalaceEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=128)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='roster.student')),
            ],
        ),
    ]