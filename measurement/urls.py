from django.urls import path

from measurement.views import SensorsView, SensorDetailView, MeasurementView

urlpatterns = [
    path('sensor/', SensorsView.as_view()),
    path('sensor/<pk>/', SensorDetailView.as_view()),
    path('measurments/', MeasurementView.as_view()),
]
