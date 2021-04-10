import csv

from django.core.management import BaseCommand

from busstations.models import Station, Route


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('moscow_bus_stations.csv', 'rt') as csv_file:
            bus_stations = list(csv.reader(csv_file, delimiter=';'))
            i = 1
            for bus_station in bus_stations[1:]:
                st = Station(name=bus_station[1], longitude=bus_station[2], latitude=bus_station[3])
                st.save()
                for route in bus_station[7].split(';'):
                    stat = Station.objects.get(pk=i)
                    route_name = Route.objects.create(name=route)
                    stat.routes.add(route_name)
                i += 1
