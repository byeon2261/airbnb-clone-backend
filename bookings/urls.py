from django.urls import path
from . import views

urlpatterns = [
    path("", views.Bookings.as_view()),
]
