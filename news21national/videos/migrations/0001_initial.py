
from south.db import db
from django.db import models
from news21national.videos.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Video'
        db.create_table('videos_video', (
            ('media_ptr', models.OneToOneField(orm['multimedia.Media'])),
            ('video', models.FileField(_('video'), null=True, max_length=255, blank=True)),
            ('hq_file', models.CharField(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('videos', ['Video'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Video'
        db.delete_table('videos_video')
        
    
    
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
        'videos.video': {
            'Meta': {'_bases': ['news21national.multimedia.models.Media']},
            'hq_file': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'media_ptr': ('models.OneToOneField', ["orm['multimedia.Media']"], {}),
            'video': ('models.FileField', ["_('video')"], {'null': 'True', 'max_length': '255', 'blank': 'True'})
        }
    }
    
    complete_apps = ['videos']
