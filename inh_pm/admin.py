from django.contrib import admin

# Register your models here.
from inh_pm.models import Bicycle, Person, Vehicle, Cyclist, Driver, Car


class PersonInline(admin.TabularInline):
    model = Person

class VehicleAdmin(admin.ModelAdmin):
    inlines = [PersonInline]

class CyclistInline(admin.TabularInline):
    model = Cyclist
    fk_name = 'transport'
    readonly_fields = ['person_ptr']


class DriverInline(admin.TabularInline):
    model = Driver
    fk_name = 'transport'
    readonly_fields = ['person_ptr']

class BicycleAdmin(admin.ModelAdmin):
    inlines = [CyclistInline]

class CarAdmin(admin.ModelAdmin):
    inlines = [DriverInline]

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Bicycle, BicycleAdmin)
admin.site.register(Car, CarAdmin)

