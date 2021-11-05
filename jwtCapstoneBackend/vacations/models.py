from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Itinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

class Review(models.Model):
    body = models.CharField(max_length=100)
    rating = models.IntegerField()
    itineraryId = models.ForeignKey(Itinerary, on_delete=models.CASCADE)