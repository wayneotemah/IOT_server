# Generated by Django 4.0.2 on 2022-10-09 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('water_reading', '0002_alter_soil_mositure_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Soil_mositure',
            new_name='Soil_moisture',
        ),
        migrations.AlterModelOptions(
            name='soil_moisture',
            options={'verbose_name': 'soil moisture', 'verbose_name_plural': 'soil moisture'},
        ),
        migrations.RenameField(
            model_name='soil_moisture',
            old_name='mositure',
            new_name='moisture',
        ),
    ]
