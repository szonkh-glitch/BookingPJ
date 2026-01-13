from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Country(models.Model):
    country_image = models.ImageField(upload_to='flags/')
    country_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.country_name


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(70)],
                                           null=True, blank=True)
    user_image = models.ImageField(upload_to='user_image/', null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    RoleChoices = (
    ('client', 'client'),
    ('owner', 'owner'))
    role = models.CharField(max_length=10, choices=RoleChoices, default='client')
    date_register = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.role}'

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=30, unique=True)
    city_image = models.ImageField(upload_to='city_images/')

    def __str__(self):
        return f'{self.country}, {self.city_name}'

class Service(models.Model):
    service_image = models.ImageField(upload_to='service_photos/')
    service_name = models.CharField(max_length=30)
    def __str__(self):
        return self.service_name

class Hotel(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotel_list')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True, related_name='countries')
    hotel_name = models.CharField(max_length=60, unique=True)
    hotel_stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    street = models.CharField(max_length=120)
    postal_code = models.PositiveSmallIntegerField(verbose_name='почтовый индекс')
    description = models.TextField()
    service = models.ManyToManyField(Service)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.hotel_name

    def get_avg_rating(self):
        review = self.hotel_review.all()
        if review.exists():
            return round(sum([i.rating for i in review]) / review.count(), 1)
        return 0

    def get_count_people(self):
        return self.hotel_review.count()

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_photo')
    hotel_image = models.ImageField(upload_to='hotel_images/')

    def __str__(self):
        return f'{self.hotel}, {self.hotel_image}'

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_rooms')
    room_number = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    RoomTypeChoices = (
    ('Люкс', 'Люкс'),
    ('Семейний', 'Семейний'),
    ('Стандарт', 'Стандарт'),
    ('Двухместный', 'Двухместный'))
    room_type = models.CharField(max_length=30, choices=RoomTypeChoices)
    RoomStatusChoices = (
    ('занят','занят'),
    ('забронирован', 'забронирован'),
    ('свободен', 'свободен'))
    room_status = models.CharField(max_length=30, choices=RoomStatusChoices)
    description = models.TextField()

    def __str__(self):
        return f'{self.hotel}, {self.room_number}'

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_photo')
    room_image = models.ImageField(upload_to='room_images/')

    def __str__(self):
        return f'{self.room}'

class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(HotelImage, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.room}, {self.hotel}'

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_review')
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i))for i in range(1, 11)])
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.rating}'

