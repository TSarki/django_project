from django.contrib import admin
from .models import Measurements, Sensor

admin.site.register(Sensor)
admin.site.register(Measurements)


