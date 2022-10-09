from django.contrib import admin
from models import Soil_mositure
# Register your models here.


class MoistureAdmin(admin.ModelAdmin):
    list_display = ('time', 'mositure')

admin.site.register(Soil_mositure,MoistureAdmin)