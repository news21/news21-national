
from south.db import db
from django.db import models
from news21national.socialchecklist.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Outlet'
        db.create_table('socialchecklist_outlet', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=150)),
            ('site_url', models.URLField(verify_exists=True)),
            ('username', models.CharField(max_length=150)),
            ('tags', models.CharField(max_length=150)),
        ))
        db.send_create_signal('socialchecklist', ['Outlet'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Outlet'
        db.delete_table('socialchecklist_outlet')
        
    
    
    models = {
        'socialchecklist.outlet': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '150'}),
            'site_url': ('models.URLField', [], {'verify_exists': 'True'}),
            'tags': ('models.CharField', [], {'max_length': '150'}),
            'username': ('models.CharField', [], {'max_length': '150'})
        }
    }
    
    complete_apps = ['socialchecklist']
