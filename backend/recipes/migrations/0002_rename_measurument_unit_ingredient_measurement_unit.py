# Generated by Django 3.2.16 on 2023-04-13 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='measurument_unit',
            new_name='measurement_unit',
        ),
    ]
