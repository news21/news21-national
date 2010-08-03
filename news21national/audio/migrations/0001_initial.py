
from south.db import db
from django.db import models
from news21national.audio.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Audio'
        db.create_table('audio_audio', (
            ('media_ptr', models.OneToOneField(orm['multimedia.Media'])),
            ('audio', models.FileField(_('audio'), max_length=255)),
        ))
        db.send_create_signal('audio', ['Audio'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Audio'
        db.delete_table('audio_audio')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'audio.audio': {
            'Meta': {'_bases': ['news21national.multimedia.models.Media']},
            'audio': ('models.FileField', ["_('audio')"], {'max_length': '255'}),
            'media_ptr': ('models.OneToOneField', ["orm['multimedia.Media']"], {})
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
    
    complete_apps = ['audio']
