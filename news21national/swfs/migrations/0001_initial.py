
from south.db import db
from django.db import models
from news21national.swfs.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Swf'
        db.create_table('swfs_swf', (
            ('media_ptr', models.OneToOneField(orm['multimedia.Media'])),
            ('loader_swf', models.CharField(max_length=255)),
            ('width', models.CharField(max_length=4)),
            ('height', models.CharField(max_length=4)),
            ('flash_compat', models.CharField("Flash Compatibility", default='9', max_length=5)),
            ('zip_file', models.FileField(storage=FileSystemStorage(), max_length=200)),
        ))
        db.send_create_signal('swfs', ['Swf'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Swf'
        db.delete_table('swfs_swf')
        
    
    
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
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'swfs.swf': {
            'Meta': {'_bases': ['news21national.multimedia.models.Media']},
            'flash_compat': ('models.CharField', ['"Flash Compatibility"'], {'default': "'9'", 'max_length': '5'}),
            'height': ('models.CharField', [], {'max_length': '4'}),
            'loader_swf': ('models.CharField', [], {'max_length': '255'}),
            'media_ptr': ('models.OneToOneField', ["orm['multimedia.Media']"], {}),
            'width': ('models.CharField', [], {'max_length': '4'}),
            'zip_file': ('models.FileField', [], {'storage': 'FileSystemStorage()', 'max_length': '200'})
        }
    }
    
    complete_apps = ['swfs']
