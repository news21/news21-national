
from south.db import db
from django.db import models
from news21national.multimedia.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Media'
        db.create_table('multimedia_media', (
            ('id', models.AutoField(primary_key=True)),
            ('_child_name', models.CharField(max_length=100, editable=False)),
            ('story', models.ForeignKey(orm['story.Story'])),
            ('title', models.CharField(max_length=128)),
            ('status', models.CharField(max_length=20)),
            ('summary', models.TextField(blank=False)),
            ('attribution', models.TextField(blank=True)),
            ('license', models.CharField(default='http://news21.com', max_length=100)),
            ('slug', models.SlugField()),
            ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="media_created_by")),
            ('created_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], related_name="media_updated_by")),
            ('updated_at', models.DateTimeField(default=datetime.datetime.now, editable=False)),
        ))
        db.send_create_signal('multimedia', ['Media'])
        
        # Adding ManyToManyField 'Media.authors'
        db.create_table('multimedia_media_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('media', models.ForeignKey(orm.Media, null=False)),
            ('user', models.ForeignKey(orm['auth.User'], null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Media'
        db.delete_table('multimedia_media')
        
        # Dropping ManyToManyField 'Media.authors'
        db.delete_table('multimedia_media_authors')
        
    
    
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
            'slug': ('models.SlugField', [], {}),
            'status': ('models.CharField', [], {'max_length': '20'}),
            'story': ('models.ForeignKey', ["orm['story.Story']"], {}),
            'summary': ('models.TextField', [], {'blank': 'False'}),
            'title': ('models.CharField', [], {'max_length': '128'}),
            'updated_at': ('models.DateTimeField', [], {'default': 'datetime.datetime.now', 'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"media_updated_by"'})
        }
    }
    
    complete_apps = ['multimedia']
