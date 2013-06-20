from django.core.management.base import BaseCommand, CommandError
from incidents.models import Incident
from xml.dom import minidom
import os

class Command(BaseCommand):
    args = '<file>'
    help = 'Parse the file for placemarks'

    def handle(self, *args, **options):
        for filename in args:
            if os.path.exists(filename):
                xml = minidom.parse(filename)
                placemarks = xml.getElementsByTagName('Placemark')
                for placemark in placemarks:
                    # create an incident
                    this_incident = Incident()
                    for child in placemark.childNodes:
                        if child.nodeName.startswith('#'):
                            continue
                        if child.nodeName != 'Point':
                            setattr(this_incident, child.nodeName, self.get_node_value(child))
                        else:
                            # get the point coordinates
                            coords = child.getElementsByTagName('coordinates')
                            if coords:
                                coords = self.get_node_value(coords[0])
                                this_incident.point_string = coords
                                this_incident.parse_point_string()


                    # check if the incident exists
                    existing_incident = Incident.objects.filter(name=this_incident.name)
                    if existing_incident:
                        this_incident.pk = existing_incident[0].pk
                    this_incident.save()

    def get_node_value(self, node):
        value = ""
        for child in node.childNodes:
            value = "%s%s" % (value, child.nodeValue)
            if child.childNodes:
                value = "%s%s" % (value, self.get_node_value(child))
        return value
