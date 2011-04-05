
from south.db import db
from django.db import models
from news21national.embed.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Embed.thirdparty'
        db.add_column('embed_embed', 'thirdparty', models.CharField(blank=True, max_length=50, null=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Embed.thirdparty'
        db.delete_column('embed_embed', 'thirdparty')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'story.story': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'multimedia.media': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'embed.embed': {
            'Meta': {'_bases': ['news21national.multimedia.models.Media']},
            'content': ('models.TextField', [], {'blank': 'False'}),
            'media_ptr': ('models.OneToOneField', ["orm['multimedia.Media']"], {}),
            'thirdparty': ('models.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'})
        }
    }
    
    complete_apps = ['embed']
