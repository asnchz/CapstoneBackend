from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Itinerary, Review, Location, ItineraryDestinations
from .serializers import ItinerarySerializer, ReviewSerializer, LocationSerializer, ItineraryDestinationsSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_itineraries(request):
    itineraries = Itinerary.objects.all()
    serializer = ItinerarySerializer(itineraries, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def user_itinerary(request):
    if request.method == 'POST':
        serializer = ItinerarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        itineraries = Itinerary.objects.filter(user_id=request.user.id)
        serializer = ItinerarySerializer(itineraries, many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_itinerary(request):
    if request.method == 'DELETE':
        itinerary = Itinerary.objects.filter(user_id=request.user.id)
        itinerary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_reviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_reviews(request):
    
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        reviews = Review.objects.filter(user_id=request.user.id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_locations(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_locations(request):
    
    if request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        locations = Location.objects.filter(user_id=request.user.id)
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_itinDestinations(request):
    itinDestinations = ItineraryDestinations.objects.all()
    serializer = ItineraryDestinationsSerializer(itinDestinations, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_itinDestinations(request):

    if request.method == 'POST':
        serializer = ItineraryDestinationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        itinDestinations = ItineraryDestinations.objects.filter(user_id=request.user.id)
        serializer = ItineraryDestinationsSerializer(itinDestinations, many=True)
        return Response(serializer.data)