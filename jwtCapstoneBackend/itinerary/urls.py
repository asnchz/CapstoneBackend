from django.urls import path
from itinerary import views

urlpatterns = [
    path('all/', views.get_all_itineraries),
    path('', views.user_itinerary),
    path('delete/', views.delete_itinerary),
    path('allreviews/', views.get_all_reviews),
    path('reviews/', views.post_review),
    path('deletereviews/', views.delete_review),
    path('location/', views.get_all_locations),
    path('userlocation', views.user_location),
    path('deletelocation/', views.delete_location),
]