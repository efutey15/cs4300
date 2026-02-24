from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    releaseDate = models.DateField()
    duration = models.PositiveIntegerField()

class Seat(models.Model):
    seatNumber = models.CharField(max_length=5)
    bookingStatus = models.BooleanField()

class Booking(models.Model):
    movie = models.CharField(max_length=30)
    seat = models.CharField(max_length=5)
    user = models.CharField(max_length=30)
    bookingDate = models.DateField()