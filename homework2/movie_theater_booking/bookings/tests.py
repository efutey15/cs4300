from django.test import TestCase
from .models import Movie, Seat

from .models import Movie, Seat

def test_double_booking_blocked(self):
    movie = Movie.objects.create(title="M", description="D", release_date="2025-01-01", duration=100)
    seat = Seat.objects.create(seatNumber="A1", bookingStatus=False)

    self.client.post("/api/bookings/", {
        "movie": movie.title,
        "seat": seat.seatNumber,
        "user": "evan"
    })

    response = self.client.post("/api/bookings/", {
        "movie": movie.title,
        "seat": seat.seatNumber,
        "user": "evan"
    })

    self.assertEqual(response.status_code, 400)