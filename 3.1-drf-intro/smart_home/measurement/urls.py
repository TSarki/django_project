from django.urls import path
from measurement.views import sensor_view_info, sensors, sensor_change, sensor_create, measure_create

urlpatterns = [
    path('sensor_change/<pk>/', sensor_change.as_view()),
    path('sensor_info/<pk>/', sensor_view_info.as_view()),
    path('sensor_create/', sensor_create.as_view()),
    path('measure_create/', measure_create.as_view()),
    path('sensors/', sensors.as_view()),

]
