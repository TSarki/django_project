from rest_framework import serializers

from .models import Sensor, Measurements

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ['sensor', 'temp', 'measure_date']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'location']
        
        

class SensorFullInfoSerializer(serializers.ModelSerializer):
    measures = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id','name','location','measures']