# Generated by Django 4.0.2 on 2022-10-10 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('water_reading', '0004_waterpump'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waterpump',
            old_name='watering',
            new_name='water_now',
        ),
    ]