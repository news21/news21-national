
from south.db import db
from django.db import models
from news21national.partner.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'StoryPlacements.screengrab'
        db.add_column('partner_storyplacements', 'screengrab', models.ImageField(_('image'), null=True, max_length=255))
        
        # Deleting field 'StoryPlacements.screengrab_url'
        db.delete_column('partner_storyplacements', 'screengrab_url')
        
        # Changing field 'StoryPlacements.description'
        db.alter_column('partner_storyplacements', 'description', models.CharField(null=True, max_length=200, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'StoryPlacements.screengrab'
        db.delete_column('partner_storyplacements', 'screengrab')
        
        # Adding field 'StoryPlacements.screengrab_url'
        db.add_column('partner_storyplacements', 'screengrab_url', models.URLField(null=True, verify_exists=False, blank=True))
        
        # Changing field 'StoryPlacements.description'
        db.alter_column('partner_storyplacements', 'description', models.CharField(max_length=200))
        
    
    
    models = {
        'partner.storyplacements': {
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"storyplacement_created_by"'}),
            'description': ('models.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'partner': ('models.ForeignKey', ["orm['partner.Partner']"], {}),
            'placement_headline': ('models.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'placement_url': ('models.URLField', [], {'blank': 'True', 'null': 'True', 'verify_exists': 'False'}),
            'screengrab': ('models.ImageField', ["_('image')"], {'null': 'True', 'max_length': '255'}),
            'story': ('models.ForeignKey', ["orm['story.Story']"], {}),
            'story_ran': ('models.DateTimeField', [], {}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"storyplacement_updated_by"'}),
            'url_active': ('models.BooleanField', [], {'default': 'True'})
        },
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'partner.partner': {
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"partner_created_by"'}),
            'email': ('models.EmailField', [], {'null': 'True', 'max_length': '150', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'members': ('models.ManyToManyField', ["orm['auth.User']"], {'related_name': '"partner_members"', 'null': 'True', 'blank': 'True'}),
            'name': ('models.CharField', [], {'max_length': '150'}),
            'phone': ('models.CharField', [], {'null': 'True', 'max_length': '25', 'blank': 'True'}),
            'site_url': ('models.URLField', [], {'verify_exists': 'True'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"partner_updated_by"'})
        },
        'story.story': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['partner']
