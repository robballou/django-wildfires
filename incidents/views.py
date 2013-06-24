from math import cos, sin, atan2, sqrt, pi
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from incidents.models import Incident
from django.contrib.staticfiles.finders import FileSystemFinder

# Create your views here.
def overview_map(request):
    incidents = Incident.objects.order_by('name')
    map_center = center_geolocation(incidents)
    template = loader.get_template('overview_map.html')
    finder = FileSystemFinder()
    perimeters = None
    perimeters_path = finder.find('fire_perimeters.json')
    if perimeters_path:
        perimeters_file = open(perimeters_path, 'r')
        perimeters = perimeters_file.read()
        perimeters_file.close()
    context = RequestContext(request, {
        'incidents': incidents,
        'map_center_lat': map_center[0],
        'map_center_lon': map_center[1],
        'fire_perimeters': perimeters
    })
    return HttpResponse(template.render(context))

def overview_data(request):
    incidents = Incident.objects.order_by('name')
    incidents_json = []
    for incident in incidents:
        incident_json = {}
        for item in incident.__dict__:
            if item.startswith('_'):
                continue
            value = getattr(incident, item)
            try:
                value = value.replace("\n", "")
                value = value.replace("\r", "")
            except:
                pass
            try:
                value = value.strftime('%Y-%m-%d')
            except:
                pass
            incident_json[item] = value
        incidents_json.append(incident_json)
    return HttpResponse(json.dumps(incidents_json), content_type="application/x-javascript")

def center_geolocation(geolocations):
    """
    Provide a relatively accurate center lat, lon returned as a list pair, given
    a list of list pairs.
    ex: in: geolocations = ((lat1,lon1), (lat2,lon2),)
        out: (center_lat, center_lon)
    """
    x = 0
    y = 0
    z = 0

    for location in geolocations:
        lat = location.point_lat * pi / 180
        lon = location.point_lon * pi / 180
        lat = float(lat)
        lon = float(lon)
        # print lat, lon
        x += cos(lat) * cos(lon)
        y += cos(lat) * sin(lon)
        z += sin(lat)

    x = float(x / len(geolocations))
    y = float(y / len(geolocations))
    z = float(z / len(geolocations))

    lon = atan2(y, x)
    hyp = sqrt(x * x + y * y)
    lat = atan2(z, hyp)

    return (lat * 180 / pi, lon * 180 / pi)
