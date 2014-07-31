from django.contrib import admin

# Register your models here.
from inh_pm.models import Bicycle, Person, Vehicle, Cyclist


class PersonInline(admin.TabularInline):
    model = Person

class VehicleAdmin(admin.ModelAdmin):
    inlines = [PersonInline]

class CyclistInline(admin.TabularInline):
    model = Cyclist

class BicycleAdmin(admin.ModelAdmin):
    inlines = [CyclistInline]

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Bicycle, BicycleAdmin)

