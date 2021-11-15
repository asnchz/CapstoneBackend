from rest_framework import serializers
from .models import Itinerary, Review, Location, ItineraryDestinations


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'details']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'body', 'rating', 'user_id']

class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        fields = ['id', 'user_id', 'details', 'review_id']

class ItineraryDestinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryDestinations
        fields = ['id', 'itinerary_id', 'location_id']
