from multiprocessing.sharedctypes import Value
from rest_framework import serializers
from .models import Soil_moisture

class WaterValueSerializer(serializers.ModelSerializer):
    class Meta:
        model =Soil_moisture
        fields='__all__'
        extra_kwargs = {"time": {"read_only": True}}
    