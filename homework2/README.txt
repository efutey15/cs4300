Project Title: Movie Booking

----------------------------------------------------------------------------------

Project Description: 
A full stack django web application allowing users to:
 - View available movies
 - Select seats and book tickets
 - View booking history
 - Access movie, seat, and booking information through a REST application
 
Verified through unit tests, integration tests, and BDD tests using behave

----------------------------------------------------------------------------------

Tech components:

Backend: Django 4.2, Python 3.12.4
API: Django REST Framework
Database: PostgreSQL
BDD Testing: Behave and behave-django
Deployment: Render

----------------------------------------------------------------------------------

Project Structure:
cs4300/
|
|--homework2/
    |
    |--movie_theater_booking/
        |
        |--bookings/
        |   |--migrations/
        |   |
        |   |--templates/
        |   |   |--bookings/ 
        |   |       |--base.html
        |   |       |--booking_history.html
        |   |       |--movie_list.html
        |   |       |seat_booking.html
        |   |
        |   |--admin.py
        |   |--apps.py
        |   |--models.py
        |   |--serializers.py
        |   |tests.py
        |   |urls_api.py
        |   |--urls.py
        |   |--views.py
        |
        |--features/
        |   |--movie_booking.feature
        |   |--steps/
        |       |--movie_booking_steps.py
        |
        |--movie_theater_booking/
        |   |--asgi.py
        |   |--settings.py
        |   |--urls.py
        |   |--wsgi.py
        |
        |--build.sh
        |--manage.py
        |--render.yaml
        |--requirements.txt

-----------------------------------------------------------------------------------
Accessing Movie Booking Live on Render:

Movie booking is live on render at the following URL:

https://mysite-6peg.onrender.com/

On the landing page, you will see all available movies. Click the 'Book Now' button
on any movie to see the available seats. After entering your name, you will be able
to book a seat. Clicking 'Movies' in the upper navigation bar will bring you back to
the available movies page. Clicking 'Booking History' will display all bookings that have
been made including the Movie, Seat, Date booked, and User.

Note: This website is being hosted using Render's free plan. The website may take
several minutes to load if there has not been traffic for more than 15 minutes.
-----------------------------------------------------------------------------------

Local development Setup (Linux based):

1. Clone Repository:

git clone https://github.com/efutey15/cs4300.git
cd cs4300/homework2/movie_theater_booking

2. Create Virtual Environment:

python3 -m venv venv-name --system-site-packages
source venv-name/bin/activate

pip install -r requirements.txt

3. Deploy using Render Blueprint based on render.yaml,
see render docs: https://render.com/docs/deploy-django