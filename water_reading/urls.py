from django.urls import path
from . import views,consumer

urlpatterns=[
    path('', views.waterReadingList, name='waterReading'),
    path('current/', views.waterReadingCurrent, name='currentWaterReading'),
    path('getcurrent/', views.waterReadingCurrentGet, name='currentWaterReading'),
    ]
