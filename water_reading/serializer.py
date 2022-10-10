from multiprocessing.sharedctypes import Value
from pyexpat import model
from rest_framework import serializers
from .models import Soil_moisture, WaterPump

class WaterValueSerializer(serializers.ModelSerializer):
    class Meta:
        model =Soil_moisture
        fields='__all__'
        extra_kwargs = {"time": {"read_only": True}}
    
class PumpSerializer(serializers.ModelSerializer):

    class Meta:
        model= WaterPump
        fields = "__all__"
    
