from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('book/<int:movie_id>/', views.book_seat, name='book_seat'),
    path('history/', views.booking_history, name='booking_history'),
]