from http.client import HTTPResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Soil_mositure
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializer import WaterValueSerializer

# Create your views here.
@api_view(['GET'])
def waterReadingList(request):
    waterValue=Soil_mositure.objects.all()
    serializer =WaterValueSerializer(waterValue, many=True)
    return Response(serializer.data)

# to get the current water value 
@api_view(['GET'])
def waterReadingCurrent(request):
    waterValue=Soil_mositure.objects.last()
    serializer =WaterValueSerializer(waterValue, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def waterReadingCurrent(request):
    waterValue=Soil_mositure.objects.last()
    serializer =WaterValueSerializer(waterValue, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def waterReadingUpdate(request):
    waterValue=request.query_params.get('Value')
    print(waterValue)
    if waterValue is not None:
        context = {
            'waterlevel':waterValue
        }
        serializer =WaterValueSerializer(data = context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)