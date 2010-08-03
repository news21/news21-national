
from south.db import db
from django.db import models
from news21national.story.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Story.secondary_image'
        db.add_column('story_story', 'secondary_image', models.IntegerField(null=True))
        
        # Adding field 'MetaStory.secondary_image'
        db.add_column('story_metastory', 'secondary_image', models.IntegerField(null=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Story.secondary_image'
        db.delete_column('story_story', 'secondary_image')
        
        # Deleting field 'MetaStory.secondary_image'
        db.delete_column('story_metastory', 'secondary_image')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'story.metastory': {
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"metastory_created_by"'}),
            'headline': ('models.CharField', [], {'max_length': '200'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'interest': ('models.TextField', [], {}),
            'is_active': ('models.BooleanField', [], {'default': 'True'}),
            'newsrooms': ('models.ManyToManyField', ["orm['newsroom.Newsroom']"], {'related_name': '"metastory_newsrooms"'}),
            'original_url': ('models.URLField', [], {'blank': 'True', 'null': 'True', 'verify_exists': 'False'}),
            'primary_image': ('models.IntegerField', [], {'null': 'True'}),
            'secondary_image': ('models.IntegerField', [], {'null': 'True'}),
            'slug': ('models.SlugField', [], {'unique': 'True'}),
            'status': ('models.CharField', [], {'default': "'Pending Approval'", 'max_length': '50'}),
            'sub_headline': ('models.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'summary': ('models.TextField', [], {}),
            'tags': ('TagField', [], {}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"metastory_updated_by"'})
        },
        'newsroom.newsroom': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'story.storypublishdate': {
            'available_at': ('models.DateTimeField', [], {}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"storydate_created_by"'}),
            'expires_at': ('models.DateTimeField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'story': ('models.ForeignKey', ["orm['story.Story']"], {}),
            'title': ('models.CharField', [], {'max_length': '200'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"storydate_updated_by"'})
        },
        'story.story': {
            'authors': ('models.ManyToManyField', ["orm['auth.User']"], {'related_name': '"story_authors"'}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"story_created_by"'}),
            'headline': ('models.CharField', [], {'max_length': '200'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'metastory': ('models.ForeignKey', ["orm['story.MetaStory']"], {}),
            'original_url': ('models.URLField', [], {'blank': 'True', 'null': 'True', 'verify_exists': 'False'}),
            'primary_image': ('models.IntegerField', [], {'null': 'True'}),
            'secondary_image': ('models.IntegerField', [], {'null': 'True'}),
            'slug': ('models.SlugField', [], {'unique': 'True'}),
            'sort': ('models.IntegerField', [], {'default': '1'}),
            'status': ('models.CharField', [], {'default': "'Pending Approval'", 'max_length': '50'}),
            'summary': ('models.TextField', [], {}),
            'tags': ('TagField', [], {}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"story_updated_by"'})
        },
        'story.storygeotag': {
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"storygeo_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'lat': ('models.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'lon': ('models.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'placement': ('models.CharField', [], {'max_length': '200'}),
            'region': ('models.CharField', [], {'max_length': '200'}),
            'story': ('models.ForeignKey', ["orm['story.Story']"], {}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"storygeo_updated_by"'})
        }
    }
    
    complete_apps = ['story']
