
from south.db import db
from django.db import models
from news21national.socialchecklist.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Scheduler'
        db.create_table('socialchecklist_scheduler', (
            ('id', models.AutoField(primary_key=True)),
            ('payload', models.ForeignKey(orm.Payload)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="socialscheduler_created_by")),
        ))
        db.send_create_signal('socialchecklist', ['Scheduler'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Scheduler'
        db.delete_table('socialchecklist_scheduler')
        
    
    
    models = {
        'socialchecklist.placement': {
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"socialplacement_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'payload': ('models.ForeignKey', ["orm['socialchecklist.Payload']"], {})
        },
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
        'multimedia.media': {
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
