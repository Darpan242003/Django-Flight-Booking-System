from django.db import models

# Create your models here.
class Flights(models.Model):
    flight_number = models.CharField(max_length=10)
    airline = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Bookings(models.Model):
    passenger_name = models.CharField(max_length=50)
    passenger_email = models.EmailField()
    passenger_phone = models.IntegerField(max_length=10)
    booking_date = models.DateTimeField(auto_now_add=True)
    is_canceled = models.BooleanField(default=False)