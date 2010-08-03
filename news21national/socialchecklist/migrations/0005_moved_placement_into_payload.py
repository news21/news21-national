
from south.db import db
from django.db import models
from news21national.socialchecklist.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Payload.placement_url'
        db.add_column('socialchecklist_payload', 'placement_url', models.CharField(max_length=400, blank=True))
        
        # Adding field 'Payload.placed_at'
        db.add_column('socialchecklist_payload', 'placed_at', models.DateTimeField(editable=False))
        
        # Adding field 'Payload.placed_by'
        db.add_column('socialchecklist_payload', 'placed_by', models.ForeignKey(orm['auth.User'], related_name="socialpayload_placed_by"))
        
        # Deleting model 'placement'
        db.delete_table('socialchecklist_placement')
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Payload.placement_url'
        db.delete_column('socialchecklist_payload', 'placement_url')
        
        # Deleting field 'Payload.placed_at'
        db.delete_column('socialchecklist_payload', 'placed_at')
        
        # Deleting field 'Payload.placed_by'
        db.delete_column('socialchecklist_payload', 'placed_by_id')
        
        # Adding model 'placement'
        db.create_table('socialchecklist_placement', (
            ('created_at', models.DateTimeField(editable=False)),
            ('id', models.AutoField(primary_key=True)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="socialplacement_created_by")),
            ('payload', models.ForeignKey(orm['socialchecklist.Payload'])),
        ))
        db.send_create_signal('socialchecklist', ['placement'])
        
    
    
    models = {
        'socialchecklist.payload': {
            'blurb': ('models.TextField', [], {}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"socialpayload_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'media': ('models.ForeignKey', ["orm['multimedia.Media']"], {}),
            'outlet': ('models.ForeignKey', ["orm['socialchecklist.Outlet']"], {}),
            'placed_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'placed_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"socialpayload_placed_by"'}),
            'placement_url': ('models.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'title': ('models.CharField', [], {'max_length': '100', 'blank': 'True'}),
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
