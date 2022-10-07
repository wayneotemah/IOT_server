from django.urls import path
from . import views,consumer

urlpatterns=[
    path('', views.waterReadingList, name='waterReading'),
    path('current/', views.waterReadingCurrent, name='currentWaterReading'),
    path('update/', views.waterReadingUpdate, name='updare Water reading'),
    ]


websocket_patterns = [
    path(r'stream/', consumer.ChatConsumer.as_asgi())
]