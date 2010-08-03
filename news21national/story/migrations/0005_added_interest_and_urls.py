
from south.db import db
from django.db import models
from news21national.story.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'MetaStory.original_url'
        db.add_column('story_metastory', 'original_url', models.URLField(verify_exists=False))
        
        # Adding field 'MetaStory.interest'
        db.add_column('story_metastory', 'interest', models.TextField())
        
        # Adding field 'Story.original_url'
        db.add_column('story_story', 'original_url', models.URLField(verify_exists=False))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'MetaStory.original_url'
        db.delete_column('story_metastory', 'original_url')
        
        # Deleting field 'MetaStory.interest'
        db.delete_column('story_metastory', 'interest')
        
        # Deleting field 'Story.original_url'
        db.delete_column('story_story', 'original_url')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'story.story': {
            'authors': ('models.ManyToManyField', ["orm['auth.User']"], {'related_name': '"story_authors"'}),
            'available_at': ('models.DateField', [], {}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"story_created_by"'}),
            'expires_at': ('models.DateField', [], {}),
            'headline': ('models.CharField', [], {'max_length': '200'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'location': ('models.CharField', [], {'max_length': '150'}),
            'metastory': ('models.ForeignKey', ["orm['story.MetaStory']"], {}),
            'original_url': ('models.URLField', [], {'verify_exists': 'False'}),
            'slug': ('models.SlugField', [], {}),
            'sort': ('models.IntegerField', [], {'default': '1'}),
            'status': ('models.CharField', [], {'max_length': '50'}),
            'summary': ('models.TextField', [], {}),
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
            'original_url': ('models.URLField', [], {'verify_exists': 'False'}),
            'slug': ('models.SlugField', [], {}),
            'sub_headline': ('models.CharField', [], {'max_length': '200'}),
            'summary': ('models.TextField', [], {}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"metastory_updated_by"'})
        },
        'newsroom.newsroom': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['story']
