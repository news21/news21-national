
from south.db import db
from django.db import models
from news21national.story.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'MetaStoryCodebase'
        db.create_table('story_metastorycodebase', (
            ('id', models.AutoField(primary_key=True)),
            ('metastory', models.ForeignKey(orm.MetaStory)),
            ('title', models.CharField(max_length=200)),
            ('description', models.TextField()),
            ('code', models.FileField(_('code'), null=True, max_length=255, blank=True)),
            ('code_url', models.URLField(blank=True, null=True, verify_exists=False)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="metastorycodebase_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], related_name="metastorycodebase_updated_by")),
            ('updated_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('story', ['MetaStoryCodebase'])
        
        # Adding model 'StoryGeoTag'
        db.create_table('story_storygeotag', (
            ('id', models.AutoField(primary_key=True)),
            ('story', models.ForeignKey(orm.Story)),
            ('placement', models.CharField(max_length=200)),
            ('region', models.CharField(max_length=200)),
            ('lat', models.DecimalField(max_digits=10, decimal_places=6)),
            ('lon', models.DecimalField(max_digits=10, decimal_places=6)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="storygeo_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], related_name="storygeo_updated_by")),
            ('updated_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('story', ['StoryGeoTag'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'MetaStoryCodebase'
        db.delete_table('story_metastorycodebase')
        
        # Deleting model 'StoryGeoTag'
        db.delete_table('story_storygeotag')
        
    
    
    models = {
        'story.metastorycodebase': {
            'code': ('models.FileField', ["_('code')"], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'code_url': ('models.URLField', [], {'blank': 'True', 'null': 'True', 'verify_exists': 'False'}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"metastorycodebase_created_by"'}),
            'description': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'metastory': ('models.ForeignKey', ["orm['story.MetaStory']"], {}),
            'title': ('models.CharField', [], {'max_length': '200'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"metastorycodebase_updated_by"'})
        },
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
            'slug': ('models.SlugField', [], {'unique': 'True'}),
            'sub_headline': ('models.CharField', [], {'max_length': '200'}),
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
        'story.story': {
            'authors': ('models.ManyToManyField', ["orm['auth.User']"], {'related_name': '"story_authors"'}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"story_created_by"'}),
            'headline': ('models.CharField', [], {'max_length': '200'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'metastory': ('models.ForeignKey', ["orm['story.MetaStory']"], {}),
            'original_url': ('models.URLField', [], {'blank': 'True', 'null': 'True', 'verify_exists': 'False'}),
            'primary_image': ('models.IntegerField', [], {'null': 'True'}),
            'slug': ('models.SlugField', [], {'unique': 'True'}),
            'sort': ('models.IntegerField', [], {'default': '1'}),
            'status': ('models.CharField', [], {'max_length': '50'}),
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
