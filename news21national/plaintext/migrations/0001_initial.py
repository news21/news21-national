
from south.db import db
from django.db import models
from news21national.plaintext.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'PlainText'
        db.create_table('plaintext_plaintext', (
            ('media_ptr', models.OneToOneField(orm['multimedia.Media'])),
            ('content', models.TextField(blank=False)),
        ))
        db.send_create_signal('plaintext', ['PlainText'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'PlainText'
        db.delete_table('plaintext_plaintext')
        
    
    
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
        'plaintext.plaintext': {
            'Meta': {'_bases': ['news21national.multimedia.models.Media']},
            'content': ('models.TextField', [], {'blank': 'False'}),
            'media_ptr': ('models.OneToOneField', ["orm['multimedia.Media']"], {})
        }
    }
    
    complete_apps = ['plaintext']
