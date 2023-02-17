from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)


class Measurements(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measures')
    temp = models.IntegerField()
    measure_date = models.DateTimeField(auto_now_add=True)

