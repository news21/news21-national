
from south.db import db
from django.db import models
from news21national.core.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Profile.created_by'
        db.add_column('core_profile', 'created_by', models.ForeignKey(orm['auth.User'], related_name="profile_created_by"))
        
        # Adding field 'Profile.updated_at'
        db.add_column('core_profile', 'updated_at', models.DateTimeField(editable=False))
        
        # Adding field 'Profile.created_at'
        db.add_column('core_profile', 'created_at', models.DateTimeField(editable=False))
        
        # Adding field 'Profile.updated_by'
        db.add_column('core_profile', 'updated_by', models.ForeignKey(orm['auth.User'], related_name="profile_updated_by"))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Profile.created_by'
        db.delete_column('core_profile', 'created_by_id')
        
        # Deleting field 'Profile.updated_at'
        db.delete_column('core_profile', 'updated_at')
        
        # Deleting field 'Profile.created_at'
        db.delete_column('core_profile', 'created_at')
        
        # Deleting field 'Profile.updated_by'
        db.delete_column('core_profile', 'updated_by_id')
        
    
    
    models = {
        'core.profile': {
            'bio': ('models.TextField', [], {}),
            'blog_uri': ('models.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"profile_created_by"'}),
            'facebookid': ('models.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'gender': ('models.BooleanField', [], {'default': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'linkedinid': ('models.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'phone': ('models.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'twitterid': ('models.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"profile_updated_by"'}),
            'user': ('models.ForeignKey', ["orm['auth.User']"], {})
        },
        'core.usersuggestedleads': {
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"usersuggestedleads_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'oulet': ('models.CharField', [], {'max_length': '200'}),
            'outlet_phone': ('models.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'outlet_uri': ('models.CharField', [], {'max_length': '300'}),
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
        'core.userskills': {
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"userskill_created_by"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'skill': ('models.ForeignKey', ["orm['core.Skill']"], {}),
            'sort': ('models.IntegerField', [], {}),
            'user': ('models.ForeignKey', ["orm['auth.User']"], {})
        }
    }
    
    complete_apps = ['core']
