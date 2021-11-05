from rest_framework import serializers
from .models import Itinerary, Review

class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        fields = ['id', 'user_id', 'location']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'body', 'rating', 'user_id']