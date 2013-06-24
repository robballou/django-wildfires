import re
from dateutil.parser import *

from django.db import models

# Create your models here.
class Incident(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    style_url = models.CharField(max_length=50)
    point_string = models.CharField(max_length=50)
    point_lat = models.FloatField()
    point_lon = models.FloatField()
    geojson = models.TextField(blank=True)
    shape = models.TextField(blank=True)
    incident_date = models.DateField(blank=True, null=True)
    fire_location = models.CharField(blank=True, max_length=150, null=True)
    fire_size = models.CharField(blank=True, max_length=150, null=True)
    fire_size_acres = models.IntegerField(blank=True, default=0)
    percent_contained = models.CharField(blank=True, max_length=150, null=True)
    fire_type = models.CharField(blank=True, max_length=150, null=True)

    def __unicode__(self):
        return self.name

    def parse_description(self):
        parts = self.description.split('<br/>')
        items = {}
        item_regex = re.compile(r'^\s*<b>([^<]+)</b> (.+)')
        for part in parts:
            match = item_regex.match(part)
            if not match:
                continue
            items[match.group(1).replace(':', '')] = match.group(2)

        if 'Report Date' in items:
            self.incident_date = parse(items['Report Date'])

        for item in items:
            item_name = item.lower().replace(' ', '_')
            try:
                setattr(self, item_name, items[item])
            except:
                pass


    def parse_point_string(self):
        point = self.point_string.split(',')
        self.point_lat = point[1]
        self.point_lon = point[0]

    def parse_size(self):
        size = re.compile(r'(\d+) acres')
        results = size.search(self.fire_size)
        if results:
            self.fire_size_acres = results.group(1)
