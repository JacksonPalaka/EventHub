from django.urls import path
from . import views
from events.views import events,reservations

urlpatterns = [
    path("",views.home),
    path("events/",events),
    path("reservations/",reservations),
]
