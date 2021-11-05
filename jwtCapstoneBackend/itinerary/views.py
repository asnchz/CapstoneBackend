from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Itinerary, Review
from .serializers import ItinerarySerializer, ReviewSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_itineraries(request):
    itineraries = Itinerary.objects.all()
    serializer = ItinerarySerializer(itineraries, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
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