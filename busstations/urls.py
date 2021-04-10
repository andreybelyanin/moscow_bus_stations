from django.urls import path

from busstations.views import view_stations

urlpatterns = [
    path('stations/', view_stations)
]
