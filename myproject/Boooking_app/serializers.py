from .models import (Country, UserProfile, City,
                     Service, Hotel, HotelImage,
                     Room, RoomImage, Booking, Review)
from rest_framework import serializers

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']

class CountryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        countries = CountryListSerializer(many=True, read_only=True)
        model = Country
        fields = '__all__'

class CountryProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_image', 'country_name']

class UserListProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'user_image', 'role']

class UserDetailProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileReviewSerializer(serializers.ModelSerializer):
    country = CountryProfileSerializer()
    class Meta:
        model = UserProfile
        fields = ['first_name', 'user_image', 'country']

class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city_name', 'city_image']

class CityHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']

class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']

class HotelListSerializer(serializers.ModelSerializer):
    city = CityHotelSerializer()
    hotel_photo = HotelImageSerializer(many=True, read_only=True)
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'hotel_photo', 'city', 'hotel_stars', 'description']

class HotelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['service_image', 'service_name']

class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'room_number', 'price', 'room_status' ,'room_type']

class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileReviewSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    class Meta:
        model = Review
        fields = ['id','user', 'text', 'created_date']

class HotelDetailSerializer(serializers.ModelSerializer):
    country = CountryListSerializer()
    city = CityHotelSerializer()
    hotel_photo = HotelImageSerializer(many=True, read_only=True)
    service = ServiceSerializer(many=True)
    hotel_rooms = RoomListSerializer(many=True, read_only=True)
    hotel_review = ReviewSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name','hotel_stars',
                  'street', 'postal_code', 'hotel_photo',
                  'description', 'city', 'country', 'service',
                  'hotel_rooms', 'get_avg_rating', 'get_count_people', 'hotel_review',]

    def get_avg_rating(self,obj):
        return obj.get_avg_rating()

    def get_count_people(self,obj):
        return obj.get_count_people()



class CityDetailSerializer(serializers.ModelSerializer):
    hotel_list = HotelListSerializer(many=True, read_only=True)
    class Meta:
        model = City
        fields = ['city_name', 'hotel_list']


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']

class RoomDetailSerializer(serializers.ModelSerializer):
    room_photo = RoomImageSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ['room_number', 'price', 'room_type',
                  'room_type', 'room_status', 'room_photo', 'description']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
