# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Race'
        db.create_table('iRFmap_race', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('race_kml', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('iRFmap', ['Race'])

        # Adding model 'Event'
        db.create_table('iRFmap_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['iRFmap.Race'])),
        ))
        db.send_create_signal('iRFmap', ['Event'])

        # Adding model 'EventDistance'
        db.create_table('iRFmap_eventdistance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('distance', self.gf('django.db.models.fields.CharField')(default='100M', max_length=4)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['iRFmap.Event'])),
        ))
        db.send_create_signal('iRFmap', ['EventDistance'])

        # Adding model 'Runner'
        db.create_table('iRFmap_runner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('iRFmap', ['Runner'])

        # Adding model 'Location'
        db.create_table('iRFmap_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('elevation', self.gf('django.db.models.fields.IntegerField')()),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=3)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=7, decimal_places=3)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('iRFmap', ['Location'])

        # Adding model 'Checkpoint'
        db.create_table('iRFmap_checkpoint', (
            ('location_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['iRFmap.Location'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('mileage', self.gf('django.db.models.fields.FloatField')()),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['iRFmap.Event'])),
        ))
        db.send_create_signal('iRFmap', ['Checkpoint'])

        # Adding model 'Country'
        db.create_table('iRFmap_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('flag', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('iRFmap', ['Country'])


    def backwards(self, orm):
        # Deleting model 'Race'
        db.delete_table('iRFmap_race')

        # Deleting model 'Event'
        db.delete_table('iRFmap_event')

        # Deleting model 'EventDistance'
        db.delete_table('iRFmap_eventdistance')

        # Deleting model 'Runner'
        db.delete_table('iRFmap_runner')

        # Deleting model 'Location'
        db.delete_table('iRFmap_location')

        # Deleting model 'Checkpoint'
        db.delete_table('iRFmap_checkpoint')

        # Deleting model 'Country'
        db.delete_table('iRFmap_country')


    models = {
        'iRFmap.checkpoint': {
            'Meta': {'object_name': 'Checkpoint', '_ormbases': ['iRFmap.Location']},
            'location_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['iRFmap.Location']", 'unique': 'True', 'primary_key': 'True'}),
            'mileage': ('django.db.models.fields.FloatField', [], {}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['iRFmap.Event']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'iRFmap.country': {
            'Meta': {'object_name': 'Country'},
            'flag': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'iRFmap.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['iRFmap.Race']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'iRFmap.eventdistance': {
            'Meta': {'object_name': 'EventDistance'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'distance': ('django.db.models.fields.CharField', [], {'default': "'100M'", 'max_length': '4'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['iRFmap.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'iRFmap.location': {
            'Meta': {'object_name': 'Location'},
            'elevation': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '3'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '3'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'iRFmap.race': {
            'Meta': {'object_name': 'Race'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'race_kml': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'iRFmap.runner': {
            'Meta': {'object_name': 'Runner'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['iRFmap']