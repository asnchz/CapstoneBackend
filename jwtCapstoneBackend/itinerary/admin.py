from django.contrib import admin
from .models import Itinerary, Review, Location, ItineraryDestinations

# Register your models here.
admin.site.register(Itinerary)
admin.site.register(Review)
admin.site.register(Location)
admin.site.register(ItineraryDestinations)