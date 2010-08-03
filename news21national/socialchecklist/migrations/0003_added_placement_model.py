
from south.db import db
from django.db import models
from news21national.socialchecklist.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Placement'
        db.create_table('socialchecklist_placement', (
            ('id', models.AutoField(primary_key=True)),
            ('payload', models.ForeignKey(orm.Payload)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="socialplacement_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('socialchecklist', ['Placement'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Placement'
        db.delete_table('socialchecklist_placement')
        
    
    
    models = {
        'socialchecklist.payload': {
            'blurb': ('models.TextField', [], {}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"socialpayload_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'media': ('models.ForeignKey', ["orm['multimedia.Media']"], {}),
            'outlet': ('models.ForeignKey', ["orm['socialchecklist.Outlet']"], {}),
            'title': ('models.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"socialpayload_updated_by"'})
        },
        'socialchecklist.placement': {
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"socialplacement_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'payload': ('models.ForeignKey', ["orm['socialchecklist.Payload']"], {})
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
        }
    }
    
    complete_apps = ['socialchecklist']
