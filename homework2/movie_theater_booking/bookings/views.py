from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import date

from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

def movie_list(request):

    """Function for displaying the movie_list template"""

    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def book_seat(request, movie_id):

    """Function for displaying the book_seat template"""

    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all()

    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seats': seats
    })

def booking_history(request):

    """Function for displaying the booking_history template"""

    bookings = Booking.objects.all()

    return render(request, 'bookings/booking_history.html', {
        'bookings': bookings
    })

class MovieViewSet(viewsets.ModelViewSet):
    """
    ViewSet for performing CRUD operations on Movie objects.

    Provides endpoints to create, retrieve, update, and delete movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Seat objects.

    Includes functionality to view seat availability and toggle the
    booking status of a specific seat.
    """
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    @action(detail=True, methods=['post'])
    def toggle_booking(self, request, pk=None):
        """
        Toggle the booking status of a seat.

        This endpoint switches the seat's bookingStatus between True and False,
        simulating seat selection and deselection during the booking process.

        Args:
            request: The HTTP request object.
            pk: The primary key of the seat to toggle.

        Returns:
            Response: A JSON response containing the seat number and its
            updated booking status.
        """
        seat = self.get_object()
        seat.bookingStatus = not seat.bookingStatus
        seat.save()

        return Response({
            "seatNumber": seat.seatNumber,
            "bookingStatus": seat.bookingStatus
        })


class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for creating bookings and retrieving booking history.

    Allows users to book seats for movies and view their past bookings.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new booking for a seat.

        Validates that the seat exists and is not already booked.
        If the seat is available, it marks the seat as booked and
        creates a Booking record.

        Args:
            request: The HTTP request object containing movie, seat,
                     and user information.

        Returns:
            Response: The created booking data if successful, or an error
            message if the seat does not exist or is already booked.
        """
        seat_number = request.data.get('seat')
        movie_title = request.data.get('movie')
        username = request.data.get('user')

        try:
            seat = Seat.objects.get(seatNumber=seat_number)
        except Seat.DoesNotExist:
            return Response({"error": "Seat not found"}, status=404)

        if seat.bookingStatus:
            return Response({"error": "Seat already booked"}, status=400)

        # Mark seat as booked
        seat.bookingStatus = True
        seat.save()

        booking = Booking.objects.create(
            movie=movie_title,
            seat=seat_number,
            user=username,
            bookingDate=date.today()
        )

        serializer = self.get_serializer(booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def history(self, request):
        """
        Retrieve booking history for a specific user.

        Expects a 'user' query parameter and returns all bookings
        associated with that username.

        Args:
            request: The HTTP request object with a 'user' query parameter.

        Returns:
            Response: A list of bookings for the specified user, or an
            error message if the user parameter is missing.
        """
        username = request.query_params.get('user')

        if not username:
            return Response({"error": "User is required"}, status=400)

        bookings = Booking.objects.filter(user=username)
        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data)