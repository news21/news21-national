
from south.db import db
from django.db import models
from news21national.api.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Key'
        db.create_table('api_key', (
            ('id', models.AutoField(primary_key=True)),
            ('content_type', models.ForeignKey(orm['contenttypes.ContentType'], related_name="content_type_set_for_%(class)s")),
            ('object_id', models.PositiveIntegerField(_('object ID'), max_length=50)),
            ('api_key', models.CharField(null=True, max_length=100, editable=False, blank=True)),
            ('is_active', models.BooleanField(default=True)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="apikey_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], related_name="apikey_updated_by")),
            ('updated_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('api', ['Key'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Key'
        db.delete_table('api_key')
        
    
    
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
        'api.key': {
            'api_key': ('models.CharField', [], {'null': 'True', 'max_length': '100', 'editable': 'False', 'blank': 'True'}),
            'content_type': ('models.ForeignKey', ["orm['contenttypes.ContentType']"], {'related_name': '"content_type_set_for_%(class)s"'}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"apikey_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('models.BooleanField', [], {'default': 'True'}),
            'object_id': ('models.PositiveIntegerField', ["_('object ID')"], {'max_length': '50'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"apikey_updated_by"'})
        }
    }
    
    complete_apps = ['api']
