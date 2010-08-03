
from south.db import db
from django.db import models
from news21national.story.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'MetaStory.tags'
        db.add_column('story_metastory', 'tags', TagField())
        
        # Adding field 'Story.tags'
        db.add_column('story_story', 'tags', TagField())
        
        # Changing field 'Story.slug'
        db.alter_column('story_story', 'slug', models.SlugField(unique=True))
        
        # Changing field 'MetaStory.slug'
        db.alter_column('story_metastory', 'slug', models.SlugField(unique=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'MetaStory.tags'
        db.delete_column('story_metastory', 'tags')
        
        # Deleting field 'Story.tags'
        db.delete_column('story_story', 'tags')
        
        # Changing field 'Story.slug'
        db.alter_column('story_story', 'slug', models.SlugField())
        
        # Changing field 'MetaStory.slug'
        db.alter_column('story_metastory', 'slug', models.SlugField())
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'story.story': {
            'authors': ('models.ManyToManyField', ["orm['auth.User']"], {'related_name': '"story_authors"'}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"story_created_by"'}),
            'headline': ('models.CharField', [], {'max_length': '200'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'metastory': ('models.ForeignKey', ["orm['story.MetaStory']"], {}),
            'original_url': ('models.URLField', [], {'blank': 'True', 'null': 'True', 'verify_exists': 'False'}),
            'slug': ('models.SlugField', [], {'unique': 'True'}),
            'sort': ('models.IntegerField', [], {'default': '1'}),
            'status': ('models.CharField', [], {'max_length': '50'}),
            'summary': ('models.TextField', [], {}),
            'tags': ('TagField', [], {}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"story_updated_by"'})
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
            'slug': ('models.SlugField', [], {'unique': 'True'}),
            'sub_headline': ('models.CharField', [], {'max_length': '200'}),
            'summary': ('models.TextField', [], {}),
            'tags': ('TagField', [], {}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"metastory_updated_by"'})
        },
        'story.storypublishdate': {
            'available_at': ('models.DateField', [], {}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"storydate_created_by"'}),
            'expires_at': ('models.DateField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'story': ('models.ForeignKey', ["orm['story.Story']"], {}),
            'title': ('models.CharField', [], {'max_length': '200'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"storydate_updated_by"'})
        },
        'newsroom.newsroom': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['story']
