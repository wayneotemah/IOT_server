from pyexpat import model
from django.db import models

# Create your models here.

class Soil_mositure(models.Model):

    mositure = models.FloatField(null=False,blank = False)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("soil mositure")
        verbose_name_plural = ("soil mositure")

    def __str__(self):
        return f"{self.time}"
