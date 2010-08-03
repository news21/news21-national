
from south.db import db
from django.db import models
from news21national.coderepo.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'CodeRepo'
        db.create_table('coderepo_coderepo', (
            ('id', models.AutoField(primary_key=True)),
            ('content_type', models.ForeignKey(orm['contenttypes.ContentType'], related_name="content_type_set_for_%(class)s")),
            ('object_id', models.PositiveIntegerField(_('object ID'), max_length=50)),
            ('title', models.CharField(max_length=200)),
            ('description', models.TextField()),
            ('code', models.FileField(_('code'), null=True, max_length=255, blank=True)),
            ('code_url', models.URLField(blank=True, null=True, verify_exists=False)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="coderepo_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], related_name="coderepo_updated_by")),
            ('updated_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('coderepo', ['CodeRepo'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'CodeRepo'
        db.delete_table('coderepo_coderepo')
        
    
    
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
        'coderepo.coderepo': {
            'code': ('models.FileField', ["_('code')"], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
            'code_url': ('models.URLField', [], {'blank': 'True', 'null': 'True', 'verify_exists': 'False'}),
            'content_type': ('models.ForeignKey', ["orm['contenttypes.ContentType']"], {'related_name': '"content_type_set_for_%(class)s"'}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"coderepo_created_by"'}),
            'description': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('models.PositiveIntegerField', ["_('object ID')"], {'max_length': '50'}),
            'title': ('models.CharField', [], {'max_length': '200'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"coderepo_updated_by"'})
        }
    }
    
    complete_apps = ['coderepo']
