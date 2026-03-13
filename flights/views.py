from django.shortcuts import render, redirect
from flights.models import Flights, Bookings
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    booked_flight = Bookings.objects.filter(is_canceled=False)

    context={
        "booked_flight":booked_flight,
             }

    return render(request, 'home.html', context)


def flights(request):
    
    from_q = request.GET.get('from')
    to_q = request.GET.get('to')

    flights = Flights.objects.all()

    if from_q:
        flights=Flights.objects.filter(source__icontains=from_q)
    if to_q:
        flights=Flights.objects.filter(destination__icontains=to_q)

    return render(request, 'flights.html', {'flights':flights})


def flight_details(request, flight_id):
    flight = Flights.objects.get(id=flight_id)

    return render(request, 'flight_details.html', {'flight':flight})



def book_flight(request, flight_id):
    flight = Flights.objects.get(id=flight_id)

    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']

            Bookings.objects.create(
                passenger_name = name,
                passenger_email = email,
                passenger_phone = phone,
            )
            return redirect('my_bookings')
    else:
        return redirect('login')

    return render(request, 'book_flight.html', {'flight':flight})


def my_bookings(request):
        
    if request.user.is_authenticated:
        if 'q' in request.GET:
            q = request.GET['q']
            bookings = Bookings.objects.filter(passenger_name__icontains = q)
        else:
            bookings = Bookings.objects.filter(is_canceled = False)
    else:
        return redirect('login')

    return render(request, 'my_bookings.html', {'bookings':bookings})



def cancel_booking(request, booking_id):
    booking = Bookings.objects.get(id=booking_id)

    return render(request, 'confirm_cancellation.html', {'booking':booking})


def confirm_cancellation(request, booking_id):
    booking = Bookings.objects.get(id=booking_id)

    if request.method == 'POST':
        booking.is_canceled = True
        booking.save()
        return redirect('my_bookings')

    return render(request, 'confirm_cancellation.html', {'booking':booking})



def flight_history(request):

    # if 'q' in request.GET:
    #     q=request.GET['q']

    bookings = Bookings.objects.filter(is_canceled=False)
    cancelled = Bookings.objects.filter(is_canceled=True)

    context={
        'bookings':bookings, 
        'cancelled':cancelled
    }

    return render(request, 'flight_history.html', context)