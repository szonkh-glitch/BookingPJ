from rest_framework.authtoken import views

from .models import (UserProfile, City,
                     Hotel,
                     Room, Booking, Review)
from .serializers import (UserListProfileSerializer, UserDetailProfileSerializer,
                          CityListSerializer, CityDetailSerializer,
                          HotelListSerializer, HotelDetailSerializer, HotelCreateSerializer,
                          RoomListSerializer, RoomCreateSerializer, RoomDetailSerializer,
                          BookingSerializer, ReviewCreateSerializer)
from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import RoomFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import HotelPagination, RoomPagination
from .permissions import CheckRolePermission, CreateHotelPermission



class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserListProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserDetailProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer

class CityDetailAPIView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer


class HotelListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['country', 'city', 'hotel_stars', 'service']
    search_fields = ['hotel_name']
    ordering_fields = ['hotel_stars']
    pagination_class = HotelPagination

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelCreateSerializer
    permission_classes = [CreateHotelPermission]

    def get_queryset(self):
        return Hotel.objects.filter()

class HotelDetailAPIView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer

class RoomListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = RoomFilter
    search_fields = ['room_number']
    ordering_fields = ['price']
    pagination_class = RoomPagination

class RoomDetailAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer

class RoomCreateViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomCreateSerializer
    permission_classes = [CreateHotelPermission]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [CheckRolePermission]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user.id)

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [CheckRolePermission]