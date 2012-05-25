# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'IPLog.expired'
        db.add_column('giraffe_iplog', 'expired',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'IPLog.expired'
        db.delete_column('giraffe_iplog', 'expired')


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
            'expired': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'giraffeword': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['giraffe.Giraffeword']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['giraffe']