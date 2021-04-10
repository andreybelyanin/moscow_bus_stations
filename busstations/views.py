from django.shortcuts import render

from busstations.models import Station, Route


def view_stations(request):
    routes_list = Route.objects.all()
    template_name = 'stations.html'
    route = request.GET.get('route')
    coordinates_dict = {}
    if route:
        target_route = Station.objects.filter(routes__name=route)
        first_longitude = float(target_route.first().longitude)
        last_longitude = float(target_route.last().longitude)
        if first_longitude > last_longitude:
            longitude_center = first_longitude - ((first_longitude - last_longitude) / 2)
        elif first_longitude < last_longitude:
            longitude_center = last_longitude - ((last_longitude - first_longitude) / 2)
        coordinates_dict['x'] = longitude_center
        first_latitude = float(target_route.first().latitude)
        last_latitude = float(target_route.last().latitude)
        if first_latitude > last_latitude:
            latitude_center = first_latitude - ((first_latitude - last_latitude) / 2)
        elif first_latitude < last_latitude:
            latitude_center = last_latitude - ((last_latitude - first_latitude) / 2)
        coordinates_dict['y'] = latitude_center
        context = {'routes': routes_list, 'stations': target_route, 'center': coordinates_dict}
    if not route:
        context = {'routes': routes_list}
    return render(request, template_name, context)
