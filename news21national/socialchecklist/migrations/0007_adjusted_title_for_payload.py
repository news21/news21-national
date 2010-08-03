
from south.db import db
from django.db import models
from news21national.socialchecklist.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Payload.title'
        db.alter_column('socialchecklist_payload', 'title', models.CharField(max_length=100, null=True, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Payload.title'
        db.alter_column('socialchecklist_payload', 'title', models.CharField(max_length=100, blank=True))
        
    
    
    models = {
        'socialchecklist.payload': {
            'blurb': ('models.TextField', [], {}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"socialpayload_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'media': ('models.ForeignKey', ["orm['multimedia.Media']"], {}),
            'outlet': ('models.ForeignKey', ["orm['socialchecklist.Outlet']"], {}),
            'placed_at': ('models.DateTimeField', [], {'null': 'True', 'editable': 'False', 'blank': 'True'}),
            'placed_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"socialpayload_placed_by"'}),
            'placement_url': ('models.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'title': ('models.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"socialpayload_updated_by"'})
        },
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'multimedia.media': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'socialchecklist.outlet': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '150'}),
            'site_url': ('models.URLField', [], {'verify_exists': 'True'}),
            'tags': ('models.CharField', [], {'max_length': '150'}),
            'username': ('models.CharField', [], {'max_length': '150'})
        },
        'socialchecklist.scheduler': {
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"socialscheduler_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'payload': ('models.ForeignKey', ["orm['socialchecklist.Payload']"], {})
        }
    }
    
    complete_apps = ['socialchecklist']
