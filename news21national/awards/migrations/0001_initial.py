
from south.db import db
from django.db import models
from news21national.awards.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Award'
        db.create_table('awards_award', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=150)),
            ('presented_by', models.CharField(max_length=150)),
            ('presented_at', models.DateTimeField()),
            ('content_type', models.ForeignKey(orm['contenttypes.ContentType'], related_name="content_type_set_for_%(class)s")),
            ('object_id', models.PositiveIntegerField(_('object ID'), max_length=50)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="award_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], related_name="award_updated_by")),
            ('updated_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('awards', ['Award'])
        
        # Adding ManyToManyField 'Award.members'
        db.create_table('awards_award_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('award', models.ForeignKey(orm.Award, null=False)),
            ('user', models.ForeignKey(orm['auth.User'], null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Award'
        db.delete_table('awards_award')
        
        # Dropping ManyToManyField 'Award.members'
        db.delete_table('awards_award_members')
        
    
    
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
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"award_updated_by"'})
        }
    }
    
    complete_apps = ['awards']
