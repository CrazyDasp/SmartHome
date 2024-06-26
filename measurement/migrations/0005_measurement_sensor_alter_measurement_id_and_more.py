# Generated by Django 5.0.3 on 2024-05-04 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_rename_datatime_measurement_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='measurementsensor',
            name='measurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements_sensor', to='measurement.measurement'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
