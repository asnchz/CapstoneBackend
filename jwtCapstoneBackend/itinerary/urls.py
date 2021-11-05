from django.urls import path
from itinerary import views

urlpatterns = [
    path('all/', views.get_all_itineraries),
    path('', views.user_itinerary),
]