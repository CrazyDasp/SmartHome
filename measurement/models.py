from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    note = models.CharField()


class Measurement(models.Model):
    temperature = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, default=1)


class MeasurementSensor(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='measurements_sensor')
