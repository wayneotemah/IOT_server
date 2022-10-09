from django.contrib import admin
from .models import Soil_moisture
# Register your models here.


class MoistureAdmin(admin.ModelAdmin):
    list_display = ('time', 'moisture')

admin.site.register(Soil_moisture,MoistureAdmin)