
from south.db import db
from django.db import models
from news21national.partner.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'StoryPlacements.screengrab'
        db.alter_column('partner_storyplacements', 'screengrab', models.ImageField(_('image'), null=True, max_length=255, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Changing field 'StoryPlacements.screengrab'
        db.alter_column('partner_storyplacements', 'screengrab', models.ImageField(_('image'), max_length=255, null=True))
        
    
    
    models = {
        'partner.storyplacements': {
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"storyplacement_created_by"'}),
            'description': ('models.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'partner': ('models.ForeignKey', ["orm['partner.Partner']"], {}),
            'placement_headline': ('models.CharField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'placement_url': ('models.URLField', [], {'blank': 'True', 'null': 'True', 'verify_exists': 'False'}),
            'screengrab': ('models.ImageField', ["_('image')"], {'null': 'True', 'max_length': '255', 'blank': 'True'}),
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
