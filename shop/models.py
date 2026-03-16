from django.db import models
from django.contrib.auth.models import User

class Plant(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='plants/')
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Review(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.comment


class PlantCare(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    sunlight = models.CharField(max_length=200)
    watering = models.TextField()
    fertilizer = models.TextField()

    def __str__(self):
        return self.plant.name