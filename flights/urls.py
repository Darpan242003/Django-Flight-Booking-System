from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flights', views.flights, name='flights'),
    path('flight_details/<int:flight_id>', views.flight_details, name='flight_details'),
    path('book_flight/<int:flight_id>', views.book_flight, name='book_flight'),
    path('my_bookings', views.my_bookings, name='my_bookings'),
    path('cancel_booking/<int:booking_id>', views.cancel_booking, name='cancel_booking'),
    path('confirm_cancellation/<int:booking_id>', views.confirm_cancellation, name='confirm_cancellation'),
    path('flight_history', views.flight_history, name='flight_history'),
]
