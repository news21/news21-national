
from south.db import db
from django.db import models
from news21national.socialchecklist.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Payload'
        db.create_table('socialchecklist_payload', (
            ('id', models.AutoField(primary_key=True)),
            ('outlet', models.ForeignKey(orm.Outlet)),
            ('media', models.ForeignKey(orm['multimedia.Media'])),
            ('title', models.CharField(max_length=100, blank=True)),
            ('blurb', models.TextField()),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="socialpayload_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], related_name="socialpayload_updated_by")),
            ('updated_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('socialchecklist', ['Payload'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Payload'
        db.delete_table('socialchecklist_payload')
        
    
    
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
