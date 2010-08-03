
from south.db import db
from django.db import models
from news21national.embed.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Embed'
        db.create_table('embed_embed', (
            ('media_ptr', models.OneToOneField(orm['multimedia.Media'])),
            ('content', models.TextField(blank=False)),
        ))
        db.send_create_signal('embed', ['Embed'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Embed'
        db.delete_table('embed_embed')
        
    
    
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
            'media_ptr': ('models.OneToOneField', ["orm['multimedia.Media']"], {})
        }
    }
    
    complete_apps = ['embed']
