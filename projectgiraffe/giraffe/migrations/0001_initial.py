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
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('added_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('giraffe', ['Giraffeword'])


    def backwards(self, orm):
        # Deleting model 'Giraffeword'
        db.delete_table('giraffe_giraffeword')


    models = {
        'giraffe.giraffeword': {
            'Meta': {'object_name': 'Giraffeword'},
            'added_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['giraffe']