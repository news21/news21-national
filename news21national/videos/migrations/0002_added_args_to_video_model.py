
from south.db import db
from django.db import models
from news21national.videos.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Video.date_taken'
        db.add_column('videos_video', 'date_taken', models.DateTimeField(null=True))
        
        # Adding field 'Video.duration'
        db.add_column('videos_video', 'duration', models.PositiveIntegerField(null=True, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Video.date_taken'
        db.delete_column('videos_video', 'date_taken')
        
        # Deleting field 'Video.duration'
        db.delete_column('videos_video', 'duration')
        
    
    
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
            'date_taken': ('models.DateTimeField', [], {'null': 'True'}),
            'duration': ('models.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hq_file': ('models.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'media_ptr': ('models.OneToOneField', ["orm['multimedia.Media']"], {}),
            'video': ('models.FileField', ["_('video')"], {'null': 'True', 'max_length': '255', 'blank': 'True'})
        }
    }
    
    complete_apps = ['videos']
