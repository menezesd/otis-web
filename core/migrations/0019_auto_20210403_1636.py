# Generated by Django 3.1.7 on 2021-04-03 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20200908_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitgroup',
            name='subject',
            field=models.CharField(choices=[('A', 'Algebra (Hufflepuff)'), ('C', 'Combinatorics (Gryffindor)'), ('G', 'Geometry (Slytherin)'), ('N', 'Number Theory (Ravenclaw)'), ('F', 'Functional Equations'), ('M', 'Miscellaneous')], help_text='The subject for the unit', max_length=2),
        ),
    ]
