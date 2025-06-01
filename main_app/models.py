from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

CATEGORIES = (
    ('exterior', 'exterior'),
    ('interior', 'interior'),
    ('suspension', 'suspension'),
    ('engine', 'engine'),
    ('drivetrain', 'drivetrain')
)

class Vehicle(models.Model):
    modelyear = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    def __str__(self):
        return self.model
    def get_absolute_url(self):
        return reverse("vehicle-detail", kwargs={"vehicle_id": self.id})
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Maintenance(models.Model):
    date = models.DateField()
    mileage = models.PositiveIntegerField()
    category = models.CharField(
        choices=CATEGORIES,
        default=CATEGORIES[0][0],
    )
    description = models.CharField(max_length=1000)

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_category_display()} at {self.mileage} on {self.date}"
    
    class Meta:
        ordering = ['-date']

