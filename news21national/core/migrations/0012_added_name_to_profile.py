
from south.db import db
from django.db import models
from news21national.core.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Profile.last_name'
        db.add_column('core_profile', 'last_name', models.CharField(max_length=75))
        
        # Adding field 'Profile.first_name'
        db.add_column('core_profile', 'first_name', models.CharField(max_length=75))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Profile.last_name'
        db.delete_column('core_profile', 'last_name')
        
        # Deleting field 'Profile.first_name'
        db.delete_column('core_profile', 'first_name')
        
    
    
    models = {
        'core.profile': {
            'address': ('models.CharField', [], {'max_length': '200'}),
            'address_city': ('models.CharField', [], {'max_length': '200'}),
            'address_state': ('models.CharField', [], {'max_length': '40'}),
            'address_zip': ('models.CharField', [], {'max_length': '20'}),
            'bio': ('models.TextField', [], {}),
            'birthdate': ('models.DateTimeField', [], {}),
            'blog_uri': ('models.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"profile_created_by"'}),
            'degree_area': ('models.CharField', [], {'default': "'Other'", 'max_length': '40'}),
            'desired_job': ('models.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ethnicity': ('models.CharField', [], {'default': "'Other'", 'max_length': '40'}),
            'expected_grad_date': ('models.DateTimeField', [], {}),
            'facebook_public': ('models.BooleanField', [], {'default': 'False'}),
            'facebookid': ('models.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'first_name': ('models.CharField', [], {'max_length': '75'}),
            'gender': ('models.CharField', [], {'default': 'False', 'max_length': '10'}),
            'hometown': ('models.CharField', [], {'max_length': '100'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('models.BooleanField', [], {'default': 'False'}),
            'last_name': ('models.CharField', [], {'max_length': '75'}),
            'linkedin_public': ('models.BooleanField', [], {'default': 'False'}),
            'linkedinid': ('models.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'non_edu_email': ('models.CharField', [], {'max_length': '200'}),
            'phone': ('models.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'school': ('models.CharField', [], {'max_length': '60'}),
            'twitter_public': ('models.BooleanField', [], {'default': 'False'}),
            'twitterid': ('models.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"profile_updated_by"'}),
            'user': ('models.ForeignKey', ["orm['auth.User']"], {}),
            'year_in_school': ('models.CharField', [], {'default': "'Other'", 'max_length': '40'})
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
