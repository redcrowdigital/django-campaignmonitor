# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Campaign.language'
        db.add_column(u'campaignmonitor_campaign', 'language',
                      self.gf('django.db.models.fields.CharField')(default='de', max_length=15),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Campaign.language'
        db.delete_column(u'campaignmonitor_campaign', 'language')


    models = {
        'campaignmonitor.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'cm_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'from_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'from_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'campaignmonitor.recipients': {
            'Meta': {'object_name': 'Recipients'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['campaignmonitor.Campaign']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'segment_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['campaignmonitor']