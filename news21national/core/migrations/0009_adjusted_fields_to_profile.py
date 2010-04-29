
from south.db import db
from django.db import models
from news21national.core.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Profile.non_edu_email'
        db.add_column('core_profile', 'non_edu_email', models.CharField(max_length=200))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Profile.non_edu_email'
        db.delete_column('core_profile', 'non_edu_email')
        
    
    
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
            'facebook_public': ('models.BooleanField', [], {'default': 'False'}),
            'facebookid': ('models.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'gender': ('models.CharField', [], {'default': 'False', 'max_length': '10'}),
            'hometown': ('models.CharField', [], {'max_length': '100'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
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
