# Generated by Django 5.0.3 on 2024-05-04 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_measurementsensor_delete_mesurmentsensor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='datatime',
            new_name='datetime',
        ),
    ]
