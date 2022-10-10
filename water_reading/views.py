from http.client import HTTPResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Soil_moisture,WaterPump
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializer import WaterValueSerializer,PumpSerializer

# Create your views here.
@api_view(['GET'])
def waterReadingList(request):
    waterValue=Soil_moisture.objects.all()
    serializer =WaterValueSerializer(waterValue, many=True)
    return Response(serializer.data)

# to get the current water value 
@api_view(['GET'])
def waterReadingCurrentGet(request):
    waterValue=Soil_moisture.objects.last()
    serializer =WaterValueSerializer(waterValue, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def waterReadingCurrent(request):
    serializer =WaterValueSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        water_now = WaterPump.objects.last()
        serializer = PumpSerializer(water_now, many=False)
        serializer.data["status"] = "Success"
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def TurnOnPump(request):
    serializer =PumpSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)