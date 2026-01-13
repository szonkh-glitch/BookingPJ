from .models import Country, City, Service, Hotel, Room, Booking, RoomImage
from modeltranslation.translator import TranslationOptions,register

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name', 'country')

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('service_name',)

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('city','country', 'hotel_name', 'street', 'description', 'service')


@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('hotel', 'description')

@register(Booking)
class BookingTranslationOptions(TranslationOptions):
    fields = ('hotel',)

@register(RoomImage)
class RoomImageTranslationOptions(TranslationOptions):
    fields = ('room',)
