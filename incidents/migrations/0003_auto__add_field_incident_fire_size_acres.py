# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Incident.fire_size_acres'
        db.add_column(u'incidents_incident', 'fire_size_acres',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Incident.fire_size_acres'
        db.delete_column(u'incidents_incident', 'fire_size_acres')


    models = {
        u'incidents.incident': {
            'Meta': {'object_name': 'Incident'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'fire_location': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'fire_size': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'fire_size_acres': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'fire_type': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'geojson': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incident_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'percent_contained': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'point_lat': ('django.db.models.fields.FloatField', [], {}),
            'point_lon': ('django.db.models.fields.FloatField', [], {}),
            'point_string': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'shape': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'style_url': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['incidents']