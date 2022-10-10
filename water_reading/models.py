from pyexpat import model
from django.db import models

# Create your models here.

class Soil_moisture(models.Model):

    moisture = models.FloatField(null=False,blank = False)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("soil moisture")
        verbose_name_plural = ("soil moisture")

    def __str__(self):
        return f"{self.time}"


class WaterPump(models.Model):

    water_now = models.BooleanField(null=False,blank = False)

    class Meta:
        verbose_name = ("Water")

    def __str__(self):
        return f"{self.watering}"
