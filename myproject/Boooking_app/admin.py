from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin
from .models import (Country, UserProfile, City, Service,
                     Hotel, HotelImage, Room, RoomImage,
                     Booking, Review)

class CityInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = City
    extra = 1
    fk_name = 'country'

class HotelImageInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = HotelImage
    extra = 1

class RoomImageInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = RoomImage
    extra = 1
    fk_name = 'room'

@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    inlines = [CityInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Hotel)
class ServiceAdmin(TranslationAdmin):
    inlines = [HotelImageInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Room)
class ServiceAdmin(TranslationAdmin):
    inlines = [RoomImageInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Service, Booking)
class ServiceAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
admin.site.register(HotelImage)
admin.site.register(Review)