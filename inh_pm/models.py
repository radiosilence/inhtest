from django.db import models
from polymorphic import PolymorphicModel
# Create your models here.

class Vehicle(PolymorphicModel):
    children = ['car', 'bicycle']
    name = models.CharField(max_length=255)
    @property
    def child(self):
        for c in self.children:
            try:
                return getattr(self, c)
            except:
                pass
        return None

class Car(Vehicle):
    engine = models.CharField(max_length=255)

class Bicycle(Vehicle):
    gears = models.PositiveIntegerField()

class Person(PolymorphicModel):
    transport = models.ForeignKey(Vehicle)
    name = models.CharField(max_length=255)

class Cyclist(Person):
    skill = models.PositiveIntegerField()