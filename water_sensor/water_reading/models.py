from django.db import models

# Create your models here.
class Value(models.Model):
    waterlevel=models.IntegerField(null=False)
    dateTime=models.DateTimeField(auto_now_add=True)

