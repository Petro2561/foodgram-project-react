# Generated by Django 3.2.16 on 2023-01-23 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_is_subscribed_customuser_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Почта'),
        ),
    ]
