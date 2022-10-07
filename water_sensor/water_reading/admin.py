from csv import list_dialects
from django.contrib import admin
from .models import Value

# Register your models here.
class ValueAdmin(admin.ModelAdmin):
    list_display=('waterlevel','dateTime')
    
admin.site.register(Value, ValueAdmin)
