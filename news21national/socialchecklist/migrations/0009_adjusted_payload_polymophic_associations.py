
from south.db import db
from django.db import models
from news21national.socialchecklist.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Payload.content_type'
        db.add_column('socialchecklist_payload', 'content_type', models.ForeignKey(orm['contenttypes.ContentType'], related_name="content_type_set_for_%(class)s"))
        
        # Adding field 'Payload.object_id'
        db.add_column('socialchecklist_payload', 'object_id', models.PositiveIntegerField(_('object ID'), max_length=50))
        
        # Deleting field 'Payload.media'
        db.delete_column('socialchecklist_payload', 'media_id')
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Payload.content_type'
        db.delete_column('socialchecklist_payload', 'content_type_id')
        
        # Deleting field 'Payload.object_id'
        db.delete_column('socialchecklist_payload', 'object_id')
        
        # Adding field 'Payload.media'
        db.add_column('socialchecklist_payload', 'media', models.ForeignKey(orm['multimedia.Media']))
        
    
    
    models = {
        'socialchecklist.payload': {
            'blurb': ('models.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('models.ForeignKey', ["orm['contenttypes.ContentType']"], {'related_name': '"content_type_set_for_%(class)s"'}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"socialpayload_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('models.PositiveIntegerField', ["_('object ID')"], {'max_length': '50'}),
            'outlet': ('models.ForeignKey', ["orm['socialchecklist.Outlet']"], {}),
            'placed_at': ('models.DateTimeField', [], {'null': 'True', 'editable': 'False', 'blank': 'True'}),
            'placed_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"socialpayload_placed_by"', 'null': 'True', 'blank': 'True'}),
            'placement_url': ('models.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'title': ('models.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"socialpayload_updated_by"'})
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
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label','model'),)", 'db_table': "'django_content_type'"},
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'socialchecklist.scheduler': {
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"socialscheduler_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'payload': ('models.ForeignKey', ["orm['socialchecklist.Payload']"], {})
        }
    }
    
    complete_apps = ['socialchecklist']
