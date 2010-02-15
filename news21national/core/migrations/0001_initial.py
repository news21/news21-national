
from south.db import db
from django.db import models
from news21national.core.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Profile'
        db.create_table('core_profile', (
            ('id', models.AutoField(primary_key=True)),
            ('user', models.ForeignKey(orm['auth.User'])),
            ('phone', models.CharField(max_length=25, blank=True)),
        ))
        db.send_create_signal('core', ['Profile'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Profile'
        db.delete_table('core_profile')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'core.profile': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'phone': ('models.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'user': ('models.ForeignKey', ["orm['auth.User']"], {})
        }
    }
    
    complete_apps = ['core']
