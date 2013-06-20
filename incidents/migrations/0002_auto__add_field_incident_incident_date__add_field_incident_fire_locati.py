# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Incident.incident_date'
        db.add_column(u'incidents_incident', 'incident_date',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Adding field 'Incident.fire_location'
        db.add_column(u'incidents_incident', 'fire_location',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True),
                      keep_default=False)

        # Adding field 'Incident.fire_size'
        db.add_column(u'incidents_incident', 'fire_size',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True),
                      keep_default=False)

        # Adding field 'Incident.percent_contained'
        db.add_column(u'incidents_incident', 'percent_contained',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True),
                      keep_default=False)

        # Adding field 'Incident.fire_type'
        db.add_column(u'incidents_incident', 'fire_type',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Incident.incident_date'
        db.delete_column(u'incidents_incident', 'incident_date')

        # Deleting field 'Incident.fire_location'
        db.delete_column(u'incidents_incident', 'fire_location')

        # Deleting field 'Incident.fire_size'
        db.delete_column(u'incidents_incident', 'fire_size')

        # Deleting field 'Incident.percent_contained'
        db.delete_column(u'incidents_incident', 'percent_contained')

        # Deleting field 'Incident.fire_type'
        db.delete_column(u'incidents_incident', 'fire_type')


    models = {
        u'incidents.incident': {
            'Meta': {'object_name': 'Incident'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'fire_location': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'}),
            'fire_size': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'}),
            'fire_type': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'}),
            'geojson': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incident_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'percent_contained': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'}),
            'point_lat': ('django.db.models.fields.FloatField', [], {}),
            'point_lon': ('django.db.models.fields.FloatField', [], {}),
            'point_string': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'shape': ('django.db.models.fields.TextField', [], {}),
            'style_url': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['incidents']