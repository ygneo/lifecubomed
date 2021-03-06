# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sighting.reported_by'
        db.add_column(u'sightings_sighting', 'reported_by',
                      self.gf('django.db.models.fields.CharField')(max_length=3000, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sighting.reported_by'
        db.delete_column(u'sightings_sighting', 'reported_by')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sightings.jellyfish': {
            'Meta': {'object_name': 'Jellyfish'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '1000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        },
        u'sightings.sighting': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Sighting'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '3000', 'null': 'True', 'blank': 'True'}),
            'image_name': ('django.db.models.fields.CharField', [], {'max_length': '3000', 'null': 'True', 'blank': 'True'}),
            'jellyfish': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sightings.Jellyfish']", 'null': 'True', 'blank': 'True'}),
            'jellyfish_quantity': ('django.db.models.fields.IntegerField', [], {'default': '2', 'null': 'True', 'blank': 'True'}),
            'jellyfish_size': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '22', 'decimal_places': '20'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '23', 'decimal_places': '20'}),
            'other_specimen_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'reported_by': ('django.db.models.fields.CharField', [], {'max_length': '3000', 'null': 'True', 'blank': 'True'}),
            'reporter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'specimen_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'thumb': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '3000', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['sightings']