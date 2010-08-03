
from south.db import db
from django.db import models
from news21national.multimedia.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Media.stage'
        db.add_column('multimedia_media', 'stage', models.CharField(default='', max_length=50, null=True, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Media.stage'
        db.delete_column('multimedia_media', 'stage')
        
    
    
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
            '_child_name': ('models.CharField', [], {'max_length': '100', 'editable': 'False'}),
            'attribution': ('models.TextField', [], {'blank': 'True'}),
            'authors': ('models.ManyToManyField', ["orm['auth.User']"], {'related_name': '"media_authors"'}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"media_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('models.BooleanField', [], {'default': 'True'}),
            'license': ('models.CharField', [], {'default': "'http://news21.com'", 'max_length': '100'}),
            'pub_date': ('models.DateTimeField', [], {'null': 'True', 'editable': 'False'}),
            'slug': ('models.SlugField', [], {'unique': 'True'}),
            'stage': ('models.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'status': ('models.CharField', [], {'default': "'Pending Approval'", 'max_length': '20'}),
            'story': ('models.ForeignKey', ["orm['story.Story']"], {}),
            'summary': ('models.TextField', [], {'blank': 'False'}),
            'tags': ('TagField', [], {}),
            'title': ('models.CharField', [], {'max_length': '128'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"media_updated_by"'})
        }
    }
    
    complete_apps = ['multimedia']
