from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    release_date = models.DateField()
    duration = models.PositiveIntegerField()

class Seat(models.Model):
    seat_number = models.CharField(max_length=5)
    booking_status = models.BooleanField()

class Booking(models.Model):
    movie = models.CharField(max_length=30)
    seat = models.CharField(max_length=5)
    user = models.CharField(max_length=30)
    booking_date = models.DateField()