from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookings.urls')),   # UI routes
    path('api/', include('bookings.urls_api')),  # API routes
]
