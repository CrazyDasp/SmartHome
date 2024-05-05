from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from measurement.models import Sensor, Measurement, MeasurementSensor
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer, \
    MeasurementDetailSerializer


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        name = request.POST.get('name')
        note = request.POST.get('note')
        Sensor(name, note).save()
        context = {'name': name, 'note': note}
        return Response(context)



class SensorDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        obj = Sensor.objects.get(pk=pk)
        new_data = request.data.get('note')
        obj.note = new_data
        obj.save()
        context = {'note': new_data}
        return Response(context)

    def get(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        measurements = Measurement.objects.filter(sensor_id=pk)

        sensor_serializer = SensorDetailSerializer(sensor)
        measurement_serializer = MeasurementDetailSerializer(measurements, many=True)
        data = {
            'id': sensor.id,
            'name': sensor.name,
            'note': sensor.note,
            'measurements': measurement_serializer.data
        }
        return Response(data)



class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        sensor_id = request.data.get('sensor')
        temperature = request.data.get('temperature')
        sensor = Sensor.objects.get(pk=sensor_id)
        measurement = Measurement.objects.create(sensor=sensor, temperature=temperature)
        serializer = self.serializer_class(measurement)
        context = {'sensor': sensor_id, 'temperature': temperature}

        return Response(context)




    