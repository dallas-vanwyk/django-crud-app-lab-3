from django.db import models
from django.urls import reverse

class Vehicle(models.Model):
    modelyear = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse("vehicle_detail", kwargs={"vehicle_id": self.id})


