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
    percent_contained = models.CharField(blank=True, max_length=150, null=True)
    fire_type = models.CharField(blank=True, max_length=150, null=True)

    def __unicode__(self):
        return self.name

