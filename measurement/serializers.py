from rest_framework import serializers

from measurement.models import Sensor, Measurement, MeasurementSensor


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['name', 'note']

class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields =['sensor', 'temperature', 'datetime']

class MeasurementDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['temperature', 'datetime']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'note', 'measurements']