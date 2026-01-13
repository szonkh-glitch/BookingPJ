from django.urls import path, include
from rest_framework import routers
from .views import (
    UserProfileListAPIView, UserProfileDetailAPIView, CityListAPIView,
    HotelListAPIView, HotelDetailAPIView,
    RoomListAPIView, RoomDetailAPIView,
    BookingViewSet, ReviewCreateAPIView, CityDetailAPIView, HotelViewSet, RoomCreateViewSet)

router = routers.DefaultRouter()
router.register('booking', BookingViewSet)
router.register('hotel_create', HotelViewSet)
router.register('room_create', RoomCreateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('hotel/', HotelListAPIView.as_view(), name='hotel-list'),
    path('hotel/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel-detail'),
    path('city/', CityListAPIView.as_view(), name='city-list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(), name='city-detail'),
    path('rooms/', RoomListAPIView.as_view(), name='room-list'),
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view(), name='room-detail'),
    path('users/', UserProfileListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user-detail'),
    path('reviews/', ReviewCreateAPIView.as_view(), name='review-create'),

]