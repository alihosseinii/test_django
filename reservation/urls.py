from django.urls import path
from .views import ReservationCreateView, ReservationListView

urlpatterns = [
    path('reservations/', ReservationCreateView.as_view(), name='reservation-create'),
    path('my-reservations/', ReservationListView.as_view(), name='reservation-list'),
]
