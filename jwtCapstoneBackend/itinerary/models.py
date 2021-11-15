from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=200)

class Review(models.Model):
    body = models.CharField(max_length=100)
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Itinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.CharField(max_length=200)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

class ItineraryDestinations(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    location =  models.ForeignKey(Location, on_delete=models.CASCADE)


