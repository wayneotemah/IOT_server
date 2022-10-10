from django.urls import path
from . import views

urlpatterns=[
    path('', views.waterReadingList, name='waterReading'),
    path('current/', views.waterReadingCurrent, name='currentWaterReading'),
    path('getcurrent/', views.waterReadingCurrentGet, name='currentWaterReading'),
    path('water_now/', views.TurnOnPump, name='water the plant now'),
    ]
