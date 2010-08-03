
from south.db import db
from django.db import models
from news21national.story.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Story'
        db.create_table('story_story', (
            ('id', models.AutoField(primary_key=True)),
            ('metastory', models.ForeignKey(orm.MetaStory)),
            ('headline', models.CharField(max_length=200)),
            ('slug', models.SlugField()),
            ('summary', models.TextField()),
            ('available_at', models.DateField()),
            ('expires_at', models.DateField()),
            ('status', models.CharField(max_length=50)),
            ('location', models.CharField(max_length=150)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="story_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], related_name="story_updated_by")),
            ('updated_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('story', ['Story'])
        
        # Adding model 'MetaStory'
        db.create_table('story_metastory', (
            ('id', models.AutoField(primary_key=True)),
            ('headline', models.CharField(max_length=200)),
            ('sub_headline', models.CharField(max_length=200)),
            ('slug', models.SlugField()),
            ('summary', models.TextField()),
            ('is_active', models.BooleanField(default=True)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="metastory_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], related_name="metastory_updated_by")),
            ('updated_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('story', ['MetaStory'])
        
        # Adding ManyToManyField 'Story.authors'
        db.create_table('story_story_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('story', models.ForeignKey(orm.Story, null=False)),
            ('user', models.ForeignKey(orm['auth.User'], null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Story'
        db.delete_table('story_story')
        
        # Deleting model 'MetaStory'
        db.delete_table('story_metastory')
        
        # Dropping ManyToManyField 'Story.authors'
        db.delete_table('story_story_authors')
        
    
    
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
            'slug': ('models.SlugField', [], {}),
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
            'is_active': ('models.BooleanField', [], {'default': 'True'}),
            'slug': ('models.SlugField', [], {}),
            'sub_headline': ('models.CharField', [], {'max_length': '200'}),
            'summary': ('models.TextField', [], {}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"metastory_updated_by"'})
        }
    }
    
    complete_apps = ['story']
