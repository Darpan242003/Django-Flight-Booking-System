from django.contrib import admin
from flights.models import Flights, Bookings

# Register your models here.
class FlightsModel(admin.ModelAdmin):
    list_display = ('flight_number', 'airline', 'source', 'destination', 'departure_time', 'arrival_time', 'price')


class BookingsModel(admin.ModelAdmin):
    list_display = ('passenger_name', 'passenger_email', 'booking_date')


admin.site.register(Flights, FlightsModel)
admin.site.register(Bookings, BookingsModel)
