from django.urls import path
from itinerary import views

urlpatterns = [
    path('all/', views.get_all_itineraries),
    path('', views.user_itinerary),
    path('delete/', views.delete_itinerary),
    path('all/', views.get_all_reviews),
    path('userreviews/', views.user_reviews),
    path('deletereview/', views.delete_review),
    path('all/', views.get_all_locations),
    path('userlocation/', views.user_locations),
    path('all/', views.get_all_itinDestinations),
    path('additindestination/', views.user_itinDestinations),
]
