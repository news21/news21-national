
from south.db import db
from django.db import models
from news21national.partner.models import *

class Migration:
    depends_on = (
        ("story", "0001_initial"),
    )

    def forwards(self, orm):
        
        # Adding model 'StoryPlacements'
        db.create_table('partner_storyplacements', (
            ('id', models.AutoField(primary_key=True)),
            ('partner', models.ForeignKey(orm.Partner)),
            ('story', models.ForeignKey(orm['story.Story'])),
            ('description', models.CharField(max_length=200)),
            ('story_ran', models.DateTimeField()),
            ('placement_url', models.URLField(blank=True, null=True, verify_exists=False)),
            ('url_active', models.BooleanField(default=True)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="storyplacement_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], related_name="storyplacement_updated_by")),
            ('updated_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('partner', ['StoryPlacements'])
        
        # Deleting field 'Partner.api_key'
        db.delete_column('partner_partner', 'api_key')
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'StoryPlacements'
        db.delete_table('partner_storyplacements')
        
        # Adding field 'Partner.api_key'
        db.add_column('partner_partner', 'api_key', models.CharField(max_length=100, null=True, editable=False, blank=True))
        
    
    
    models = {
        'partner.storyplacements': {
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"storyplacement_created_by"'}),
            'description': ('models.CharField', [], {'max_length': '200'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'partner': ('models.ForeignKey', ["orm['partner.Partner']"], {}),
            'placement_url': ('models.URLField', [], {'blank': 'True', 'null': 'True', 'verify_exists': 'False'}),
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
            'email': ('models.EmailField', [], {'max_length': '150'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'members': ('models.ManyToManyField', ["orm['auth.User']"], {'related_name': '"partner_members"', 'null': 'True', 'blank': 'True'}),
            'name': ('models.CharField', [], {'max_length': '150'}),
            'phone': ('models.CharField', [], {'max_length': '25'}),
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
