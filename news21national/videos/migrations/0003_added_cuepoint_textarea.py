
from south.db import db
from django.db import models
from news21national.videos.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Video.cuepoints'
        db.add_column('videos_video', 'cuepoints', models.TextField(null=True, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Video.cuepoints'
        db.delete_column('videos_video', 'cuepoints')
        
    
    
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
            'cuepoints': ('models.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_taken': ('models.DateTimeField', [], {'null': 'True'}),
            'duration': ('models.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hq_file': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'media_ptr': ('models.OneToOneField', ["orm['multimedia.Media']"], {}),
            'video': ('models.FileField', ["_('video')"], {'null': 'True', 'max_length': '255', 'blank': 'True'})
        }
    }
    
    complete_apps = ['videos']
