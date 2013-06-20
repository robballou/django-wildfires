# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Incident'
        db.create_table(u'incidents_incident', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('style_url', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('point_string', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('point_lat', self.gf('django.db.models.fields.FloatField')()),
            ('point_lon', self.gf('django.db.models.fields.FloatField')()),
            ('geojson', self.gf('django.db.models.fields.TextField')()),
            ('shape', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'incidents', ['Incident'])


    def backwards(self, orm):
        # Deleting model 'Incident'
        db.delete_table(u'incidents_incident')


    models = {
        u'incidents.incident': {
            'Meta': {'object_name': 'Incident'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'geojson': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'point_lat': ('django.db.models.fields.FloatField', [], {}),
            'point_lon': ('django.db.models.fields.FloatField', [], {}),
            'point_string': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'shape': ('django.db.models.fields.TextField', [], {}),
            'style_url': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['incidents']