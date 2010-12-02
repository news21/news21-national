
from south.db import db
from django.db import models
from news21national.newsroom.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'NewsOrganization.shorter_code'
        db.add_column('newsroom_newsorganization', 'shorter_code', models.CharField(max_length=10, null=True, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'NewsOrganization.shorter_code'
        db.delete_column('newsroom_newsorganization', 'shorter_code')
        
    
    
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
            'members': ('models.ManyToManyField', ["orm['auth.User']"], {'related_name': '"newsroom_members"', 'null': 'True', 'blank': 'True'}),
            'name': ('models.CharField', [], {'max_length': '150'}),
            'organization': ('models.ForeignKey', ["orm['newsroom.NewsOrganization']"], {'related_name': '"newsroom_newsorganization"', 'null': 'True', 'blank': 'True'}),
            'short_name': ('models.CharField', [], {'max_length': '150'}),
            'shorter_code': ('models.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'site_url': ('models.URLField', [], {'verify_exists': 'True'}),
            'tags': ('TagField', [], {}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"newsroom_updated_by"'})
        },
        'newsroom.newsorganization': {
            'bio': ('models.TextField', [], {}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"newsorganization_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '150'}),
            'shorter_code': ('models.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'site_url': ('models.URLField', [], {'verify_exists': 'True'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"newsorganization_updated_by"'})
        }
    }
    
    complete_apps = ['newsroom']
