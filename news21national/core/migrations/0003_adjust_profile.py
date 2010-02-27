
from south.db import db
from django.db import models
from news21national.core.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Profile.twitterid'
        db.alter_column('core_profile', 'twitterid', models.CharField(max_length=200, blank=True))
        
        # Changing field 'Profile.blog_uri'
        db.alter_column('core_profile', 'blog_uri', models.CharField(max_length=300, blank=True))
        
        # Changing field 'Profile.facebookid'
        db.alter_column('core_profile', 'facebookid', models.CharField(max_length=200, blank=True))
        
        # Changing field 'Profile.linkedinid'
        db.alter_column('core_profile', 'linkedinid', models.CharField(max_length=200, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Profile.twitterid'
        db.alter_column('core_profile', 'twitterid', models.CharField(max_length=200))
        
        # Changing field 'Profile.blog_uri'
        db.alter_column('core_profile', 'blog_uri', models.CharField(max_length=300))
        
        # Changing field 'Profile.facebookid'
        db.alter_column('core_profile', 'facebookid', models.CharField(max_length=200))
        
        # Changing field 'Profile.linkedinid'
        db.alter_column('core_profile', 'linkedinid', models.CharField(max_length=200))
        
    
    
    models = {
        'core.profile': {
            'bio': ('models.TextField', [], {}),
            'blog_uri': ('models.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'facebookid': ('models.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'gender': ('models.BooleanField', [], {'default': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'linkedinid': ('models.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'phone': ('models.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'twitterid': ('models.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('models.ForeignKey', ["orm['auth.User']"], {})
        },
        'core.userskills': {
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"userskill_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'skill': ('models.ForeignKey', ["orm['core.Skill']"], {}),
            'sort': ('models.IntegerField', [], {}),
            'user': ('models.ForeignKey', ["orm['auth.User']"], {})
        },
        'core.skill': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'title': ('models.CharField', [], {'max_length': '200'})
        },
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'core.usersuggestedleads': {
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"usersuggestedleads_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'oulet': ('models.CharField', [], {'max_length': '200'}),
            'outlet_phone': ('models.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'outlet_uri': ('models.CharField', [], {'max_length': '300'}),
            'user': ('models.ForeignKey', ["orm['auth.User']"], {})
        }
    }
    
    complete_apps = ['core']
