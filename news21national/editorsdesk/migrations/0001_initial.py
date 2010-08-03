
from south.db import db
from django.db import models
from news21national.editorsdesk.models import *

class Migration:
    depends_on = (
        ("newsroom", "0001_initial"),
    )

    def forwards(self, orm):
        
        # Adding model 'EditorsDesk'
        db.create_table('editorsdesk_editorsdesk', (
            ('id', models.AutoField(primary_key=True)),
            ('newsroom', models.ForeignKey(orm['newsroom.Newsroom'])),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="editorsdesk_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], related_name="editorsdesk_updated_by")),
            ('updated_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('editorsdesk', ['EditorsDesk'])
        
        # Adding ManyToManyField 'EditorsDesk.editors'
        db.create_table('editorsdesk_editorsdesk_editors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('editorsdesk', models.ForeignKey(orm.EditorsDesk, null=False)),
            ('user', models.ForeignKey(orm['auth.User'], null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'EditorsDesk'
        db.delete_table('editorsdesk_editorsdesk')
        
        # Dropping ManyToManyField 'EditorsDesk.editors'
        db.delete_table('editorsdesk_editorsdesk_editors')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'editorsdesk.editorsdesk': {
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"editorsdesk_created_by"'}),
            'editors': ('models.ManyToManyField', ["orm['auth.User']"], {'related_name': '"editorsdesk_editors"', 'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'newsroom': ('models.ForeignKey', ["orm['newsroom.Newsroom']"], {}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"editorsdesk_updated_by"'})
        },
        'newsroom.newsroom': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['editorsdesk']
