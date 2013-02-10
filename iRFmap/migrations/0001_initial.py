# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table('iRFmap_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('race_kml', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
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

        # Adding model 'Person'
        db.create_table('iRFmap_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('iRFmap', ['Person'])

        # Adding model 'Runner'
        db.create_table('iRFmap_runner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['iRFmap.Person'])),
        ))
        db.send_create_signal('iRFmap', ['Runner'])

        # Adding model 'Race'
        db.create_table('iRFmap_race', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['iRFmap.Event'])),
        ))
        db.send_create_signal('iRFmap', ['Race'])

        # Adding M2M table for field runners on 'Race'
        db.create_table('iRFmap_race_runners', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('race', models.ForeignKey(orm['iRFmap.race'], null=False)),
            ('runner', models.ForeignKey(orm['iRFmap.runner'], null=False))
        ))
        db.create_unique('iRFmap_race_runners', ['race_id', 'runner_id'])

        # Adding model 'RunnerStatus'
        db.create_table('iRFmap_runnerstatus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('runner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['iRFmap.Runner'])),
        ))
        db.send_create_signal('iRFmap', ['RunnerStatus'])

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
        # Deleting model 'Event'
        db.delete_table('iRFmap_event')

        # Deleting model 'EventDistance'
        db.delete_table('iRFmap_eventdistance')

        # Deleting model 'Person'
        db.delete_table('iRFmap_person')

        # Deleting model 'Runner'
        db.delete_table('iRFmap_runner')

        # Deleting model 'Race'
        db.delete_table('iRFmap_race')

        # Removing M2M table for field runners on 'Race'
        db.delete_table('iRFmap_race_runners')

        # Deleting model 'RunnerStatus'
        db.delete_table('iRFmap_runnerstatus')

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
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'race_kml': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        'iRFmap.person': {
            'Meta': {'object_name': 'Person'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        },
        'iRFmap.race': {
            'Meta': {'object_name': 'Race'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['iRFmap.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'runners': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['iRFmap.Runner']", 'symmetrical': 'False'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'iRFmap.runner': {
            'Meta': {'object_name': 'Runner'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['iRFmap.Person']"}),
            'position': ('django.db.models.fields.IntegerField', [], {})
        },
        'iRFmap.runnerstatus': {
            'Meta': {'object_name': 'RunnerStatus'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'runner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['iRFmap.Runner']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['iRFmap']