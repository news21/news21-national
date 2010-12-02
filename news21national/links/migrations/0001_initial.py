
from south.db import db
from django.db import models
from news21national.links.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Link'
        db.create_table('links_link', (
            ('media_ptr', models.OneToOneField(orm['multimedia.Media'])),
            ('url', models.URLField(verify_exists=True)),
        ))
        db.send_create_signal('links', ['Link'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Link'
        db.delete_table('links_link')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'links.link': {
            'Meta': {'_bases': ['news21national.multimedia.models.Media']},
            'media_ptr': ('models.OneToOneField', ["orm['multimedia.Media']"], {}),
            'url': ('models.URLField', [], {'verify_exists': 'True'})
        },
        'multimedia.media': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'story.story': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['links']
