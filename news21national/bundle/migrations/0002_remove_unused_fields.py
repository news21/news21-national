
from south.db import db
from django.db import models
from news21national.bundle.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Deleting field 'StoryBundle.tags'
        db.delete_column('bundle_storybundle', 'tags')
        
        # Dropping ManyToManyField 'StoryBundle.newsrooms'
        db.delete_table('bundle_storybundle_newsrooms')
        
    
    
    def backwards(self, orm):
        
        # Adding field 'StoryBundle.tags'
        db.add_column('bundle_storybundle', 'tags', TagField())
        
        # Adding ManyToManyField 'StoryBundle.newsrooms'
        db.create_table('bundle_storybundle_newsrooms', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('storybundle', models.ForeignKey(orm.StoryBundle, null=False)),
            ('newsroom', models.ForeignKey(orm['newsroom.newsroom'], null=False))
        ))
        
    
    
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
            'slug': ('models.SlugField', [], {'unique': 'True'}),
            'stories': ('models.ManyToManyField', ["orm['story.Story']"], {}),
            'title': ('models.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"bundles_updated_by"'})
        }
    }
    
    complete_apps = ['bundle']
