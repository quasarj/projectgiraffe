# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Giraffeword'
        db.create_table('giraffe_giraffeword', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=400, null=True)),
            ('added_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('giraffe', ['Giraffeword'])

        # Adding model 'IPLog'
        db.create_table('giraffe_iplog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('giraffeword', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['giraffe.Giraffeword'])),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('added_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('giraffe', ['IPLog'])


    def backwards(self, orm):
        # Deleting model 'Giraffeword'
        db.delete_table('giraffe_giraffeword')

        # Deleting model 'IPLog'
        db.delete_table('giraffe_iplog')


    models = {
        'giraffe.giraffeword': {
            'Meta': {'object_name': 'Giraffeword'},
            'added_date': ('django.db.models.fields.DateTimeField', [], {}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'giraffe.iplog': {
            'Meta': {'object_name': 'IPLog'},
            'added_date': ('django.db.models.fields.DateTimeField', [], {}),
            'giraffeword': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['giraffe.Giraffeword']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['giraffe']