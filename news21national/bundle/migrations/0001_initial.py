
from south.db import db
from django.db import models
from news21national.bundle.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'StoryBundle'
        db.create_table('bundle_storybundle', (
            ('id', models.AutoField(primary_key=True)),
            ('title', models.CharField(max_length=200, null=True, blank=True)),
            ('slug', models.SlugField(unique=True)),
            ('tags', TagField()),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="bundles_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], related_name="bundles_updated_by")),
            ('updated_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('bundle', ['StoryBundle'])
        
        # Adding ManyToManyField 'StoryBundle.stories'
        db.create_table('bundle_storybundle_stories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('storybundle', models.ForeignKey(orm.StoryBundle, null=False)),
            ('story', models.ForeignKey(orm['story.Story'], null=False))
        ))
        
        # Adding ManyToManyField 'StoryBundle.newsrooms'
        db.create_table('bundle_storybundle_newsrooms', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('storybundle', models.ForeignKey(orm.StoryBundle, null=False)),
            ('newsroom', models.ForeignKey(orm['newsroom.Newsroom'], null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'StoryBundle'
        db.delete_table('bundle_storybundle')
        
        # Dropping ManyToManyField 'StoryBundle.stories'
        db.delete_table('bundle_storybundle_stories')
        
        # Dropping ManyToManyField 'StoryBundle.newsrooms'
        db.delete_table('bundle_storybundle_newsrooms')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'story.story': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'newsroom.newsroom': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'bundle.storybundle': {
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"bundles_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'newsrooms': ('models.ManyToManyField', ["orm['newsroom.Newsroom']"], {'related_name': '"bundles_newsrooms"', 'null': 'True', 'blank': 'True'}),
            'slug': ('models.SlugField', [], {'unique': 'True'}),
            'stories': ('models.ManyToManyField', ["orm['story.Story']"], {}),
            'tags': ('TagField', [], {}),
            'title': ('models.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"bundles_updated_by"'})
        }
    }
    
    complete_apps = ['bundle']
