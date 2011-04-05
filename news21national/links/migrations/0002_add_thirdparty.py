
from south.db import db
from django.db import models
from news21national.links.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Link.thirdparty'
        db.add_column('links_link', 'thirdparty', models.CharField(blank=True, max_length=50, null=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Link.thirdparty'
        db.delete_column('links_link', 'thirdparty')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'links.link': {
            'Meta': {'_bases': ['news21national.multimedia.models.Media']},
            'media_ptr': ('models.OneToOneField', ["orm['multimedia.Media']"], {}),
            'thirdparty': ('models.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
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
