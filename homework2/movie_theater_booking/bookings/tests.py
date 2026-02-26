from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import date

from .models import Movie, Seat, Booking

class ModelTests(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="This is a Test!",
            release_date=date.today(),
            duration=100
        )

        self.seat = Seat.objects.create(
            seat_number=1,
            booking_status=False
        )
    
    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Test Movie")
    
    def test_seat_default_status(self):
        self.assertFalse(self.seat.booking_status)
    
    def test_booking_creation(self):
        booking = Booking.objects.create(
            movie="Test Movie",
            seat=1,
            user="evan",
            booking_date=date.today()
        )

        self.assertEqual(booking.user, "evan")
        self.assertEqual(booking.seat, 1)
    
    
class APITests(APITestCase):

    def setUp(self):
        self.movie = Movie.objects.create(
            title="API Movie",
            description="API Movie Test",
            release_date=date.today(),
            duration=100
        )

        self.seat = Seat.objects.create(
            seat_number=10,
            booking_status=False
        )
    
    def test_get_movies_list(self):
        response = self.client.get("/api/movies")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
    
    def test_create_movie(self):
        data = {
            "title": "New Movie",
            "release_date": str(date.today())
        }
        response = self.client.post("/api/movies/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_seats(self):
        response = self.client.get("/api/seats/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_toggle_seat_booking(self):
        response = self.client.post(f"/api/seats/{self.seat.id}/toggle_booking/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.seat.refresh_from_db()
        self.assertTrue(self.seat.booking_status)
    
    def test_create_booking_success(self):
        data = {
            "movie": "API Movie",
            "seat": 10,
            "user": "evan"
        }

        response = self.client.post("/api/bookings/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.seat.refresh_from_db()
        self.assertTrue(self.seat.booking_status)
    
    def test_create_booking_invalid_seat(self):
        data = {
            "movie": "API Movie",
            "seat": 999,
            "user": "evan"
        }

        response = self.client.post("/api/bookings/", data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_create_booking_already_booked(self):
        self.seat.booking_status = True
        self.seat.save()

        data = {
            "movie": "API Movie",
            "seat": 10,
            "user": "evan"
        }

        response = self.client.post("/api/bookings/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_booking_history_success(self):
        Booking.objects.create(
            movie="API Movie",
            seat=10,
            user="evan",
            booking_date=date.today()
        )

        response = self.client.get("/api/bookings/history/?user=evan")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_booking_history_missing_user(self):
        response = self.client.get("/api/bookings/history/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)