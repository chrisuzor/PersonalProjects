# vehicle/admin.py
from django.contrib import admin

from .models import Part, Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    pass
