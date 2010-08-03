
from south.db import db
from django.db import models
from news21national.multimedia.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Deleting field 'Media.slug'
        db.delete_column('multimedia_media', 'slug')
        
    
    
    def backwards(self, orm):
        
        # Adding field 'Media.slug'
        db.add_column('multimedia_media', 'slug', models.SlugField())
        
    
    
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
            'created_at': ('models.DateTimeField', [], {'default': 'datetime.datetime.now', 'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"media_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'license': ('models.CharField', [], {'default': "'http://news21.com'", 'max_length': '100'}),
            'pub_date': ('models.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'status': ('models.CharField', [], {'max_length': '20'}),
            'story': ('models.ForeignKey', ["orm['story.Story']"], {}),
            'summary': ('models.TextField', [], {'blank': 'False'}),
            'title': ('models.CharField', [], {'max_length': '128'}),
            'updated_at': ('models.DateTimeField', [], {'default': 'datetime.datetime.now', 'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"media_updated_by"'})
        }
    }
    
    complete_apps = ['multimedia']
