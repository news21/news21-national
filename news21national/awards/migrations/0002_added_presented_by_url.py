
from south.db import db
from django.db import models
from news21national.awards.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Award.presented_url'
        db.add_column('awards_award', 'presented_url', models.URLField(blank=True, null=True, verify_exists=False))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Award.presented_url'
        db.delete_column('awards_award', 'presented_url')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label','model'),)", 'db_table': "'django_content_type'"},
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'awards.award': {
            'content_type': ('models.ForeignKey', ["orm['contenttypes.ContentType']"], {'related_name': '"content_type_set_for_%(class)s"'}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"award_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'members': ('models.ManyToManyField', ["orm['auth.User']"], {'related_name': '"award_members"', 'null': 'True', 'blank': 'True'}),
            'name': ('models.CharField', [], {'max_length': '150'}),
            'object_id': ('models.PositiveIntegerField', ["_('object ID')"], {'max_length': '50'}),
            'presented_at': ('models.DateTimeField', [], {}),
            'presented_by': ('models.CharField', [], {'max_length': '150'}),
            'presented_url': ('models.URLField', [], {'blank': 'True', 'null': 'True', 'verify_exists': 'False'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"award_updated_by"'})
        }
    }
    
    complete_apps = ['awards']
