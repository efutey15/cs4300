from behave import given, when, then
from django.test import Client
from bookings.models import Movie, Seat, Booking

client = Client()
response = None
movie = None

'''First Scenario: Choosing a movie '''

@given('I have a movie named wicked')
def step_create_movie(context):
    global movie
    movie = Movie.objects.create(
        title="wicked",
        description="Test movie",
        release_date="2025-01-01",
        duration=120
    )

    # Create seats
    for i in range(1, 6):
        Seat.objects.create(seat_number=f"A{i}", booking_status=False)


@when('I click Book Now')
def step_click_book_now(context):
    global response
    response = client.get(f"/book/{movie.id}/")


@then('I can see available seats for wicked')
def step_see_seats(context):
    assert response.status_code == 200
    assert b"wicked" in response.content
    assert b"A1" in response.content


'''Second Scenario: Reserving a seat '''
@given('I am on the wicked seat booking screen')
def step_go_to_seat_page(context):
    context.movie = Movie.objects.create(
        title="wicked",
        description="Test movie",
        release_date="2025-01-01",
        duration=120
    )

    Seat.objects.create(seat_number="A1", booking_status=False)

    context.response = client.get(f"/book/{context.movie.id}/")
    assert context.response.status_code == 200


@given('my name is Evan')
def step_store_name(context):
    context.username = "Evan"


@when('I enter my name')
def step_noop(context):
    pass


@when('I select seat A1')
def step_book_seat(context):
    context.response = client.post(
        f"/book/{context.movie.id}/",
        {
            "user": context.username,
            "seat_number": "A1"
        },
        follow=True
    )


@then('the seat A1 should be booked')
def step_check_booking(context):
    seat = Seat.objects.get(seat_number="A1")
    assert seat.booking_status is True

    booking = Booking.objects.filter(
        user="Evan",
        seat="A1",
        movie="wicked"
    ).exists()

    assert booking is True

'''Third Scenario: Attempting to reserve a seat that is already reserved '''

@given('seat A1 is already booked')
def step_already_booked(context):
    seat = Seat.objects.get(seat_number="A1")
    seat.booking_status = True
    seat.save()


@when('I try to book seat A1')
def step_try_booking_again(context):
    context.response = client.post(
        f"/book/{context.movie.id}/",
        {
            "user": context.username,
            "seat_number": "A1"
        },
        follow=True
    )


@then('the booking should not be created')
def step_no_booking_created(context):
    booking_count = Booking.objects.filter(
        user=context.username,
        seat="A1",
        movie="wicked"
    ).count()

    assert booking_count == 0


@then('the seat A1 should remain booked')
def step_seat_still_booked(context):
    seat = Seat.objects.get(seat_number="A1")
    assert seat.booking_status is True