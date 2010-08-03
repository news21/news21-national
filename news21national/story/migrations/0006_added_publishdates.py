
from south.db import db
from django.db import models
from news21national.story.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'StoryPublishDate'
        db.create_table('story_storypublishdate', (
            ('id', models.AutoField(primary_key=True)),
            ('story', models.ForeignKey(orm.Story)),
            ('title', models.CharField(max_length=200)),
            ('available_at', models.DateField()),
            ('expires_at', models.DateField()),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="storydate_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('story', ['StoryPublishDate'])
        
        # Deleting field 'Story.expires_at'
        db.delete_column('story_story', 'expires_at')
        
        # Deleting field 'Story.available_at'
        db.delete_column('story_story', 'available_at')
        
        # Changing field 'MetaStory.original_url'
        db.alter_column('story_metastory', 'original_url', models.URLField(blank=True, null=True, verify_exists=False))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'StoryPublishDate'
        db.delete_table('story_storypublishdate')
        
        # Adding field 'Story.expires_at'
        db.add_column('story_story', 'expires_at', models.DateField())
        
        # Adding field 'Story.available_at'
        db.add_column('story_story', 'available_at', models.DateField())
        
        # Changing field 'MetaStory.original_url'
        db.alter_column('story_metastory', 'original_url', models.URLField(verify_exists=False))
        
    
    
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
            'original_url': ('models.URLField', [], {'blank': 'True', 'null': 'True', 'verify_exists': 'False'}),
            'slug': ('models.SlugField', [], {}),
            'sub_headline': ('models.CharField', [], {'max_length': '200'}),
            'summary': ('models.TextField', [], {}),
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
            'title': ('models.CharField', [], {'max_length': '200'})
        },
        'newsroom.newsroom': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['story']
