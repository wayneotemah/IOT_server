from multiprocessing.sharedctypes import Value
from rest_framework import serializers
from .models import Value

class WaterValueSerializer(serializers.ModelSerializer):
    class Meta:
        model =Value
        fields='__all__'
        extra_kwargs = {"dateTime": {"read_only": True}}
    