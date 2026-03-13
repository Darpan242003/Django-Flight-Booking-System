# Flight Booking System

A web-based flight reservation system built using Django that allows users to search flights, select seats, and manage bookings through a secure authentication system.

## Overview

The Flight Booking System is a web application that enables users to search for flights, view available options, select seats, and book flights. The system manages user authentication, flight details, and booking records using Django ORM and SQLite.

## Features

- User registration and authentication
- Flight search functionality
- Seat selection and booking management
- Secure booking workflow
- Database operations using Django ORM
- Admin panel for managing flights and bookings

## Tech Stack

Backend: Django (Python)  
Database: SQLite  
ORM: Django ORM  
Frontend: HTML, CSS, Bootstrap  
Version Control: Git & GitHub

## Project Structure

flight-booking-system/
│
├── flights/        # Flight management app
├── bookings/       # Booking and reservation logic
├── users/          # Authentication system
├── templates/      # HTML templates
├── static/         # CSS and assets
├── db.sqlite3      # Database file
└── manage.py       # Django project manager

## Installation

1. Clone the repository

git clone https://github.com/yourusername/flight-booking-system.git

2. Navigate to project folder

cd flight-booking-system

3. Install dependencies

pip install -r requirements.txt

4. Run migrations

python manage.py migrate

5. Start the server

python manage.py runserver

## Screenshots

Login Page  
<img width="1920" height="1040" alt="Flight Booking Home Page" src="https://github.com/user-attachments/assets/c036650c-3ab0-40c8-88af-ebaa7144e183" />
Flight Search Page  
Booking Confirmation Page


## Future Improvements

- Integrate payment gateway
- Implement REST APIs using Django REST Framework
- Deploy the application on cloud platforms
- Add real-time flight availability updates

## Author

Darpan Bhamre  
LinkedIn: https://linkedin.com/in/darpanbhamre  
GitHub: https://github.com/Darpan242003
