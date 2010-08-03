
from south.db import db
from django.db import models
from news21national.newsroom.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Newsroom'
        db.create_table('newsroom_newsroom', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=150)),
            ('short_name', models.CharField(max_length=150)),
            ('site_url', models.URLField(verify_exists=True)),
            ('bio', models.TextField()),
            ('is_active', models.BooleanField(default=True)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="newsroom_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], related_name="newsroom_updated_by")),
            ('updated_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('newsroom', ['Newsroom'])
        
        # Adding ManyToManyField 'Newsroom.members'
        db.create_table('newsroom_newsroom_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsroom', models.ForeignKey(orm.Newsroom, null=False)),
            ('user', models.ForeignKey(orm['auth.User'], null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Newsroom'
        db.delete_table('newsroom_newsroom')
        
        # Dropping ManyToManyField 'Newsroom.members'
        db.delete_table('newsroom_newsroom_members')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'newsroom.newsroom': {
            'bio': ('models.TextField', [], {}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"newsroom_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('models.BooleanField', [], {'default': 'True'}),
            'members': ('models.ManyToManyField', ["orm['auth.User']"], {'related_name': '"newsroom_members"'}),
            'name': ('models.CharField', [], {'max_length': '150'}),
            'short_name': ('models.CharField', [], {'max_length': '150'}),
            'site_url': ('models.URLField', [], {'verify_exists': 'True'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"newsroom_updated_by"'})
        }
    }
    
    complete_apps = ['newsroom']
