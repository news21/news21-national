
from south.db import db
from django.db import models
from news21national.core.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Profile.linkedin_public'
        db.add_column('core_profile', 'linkedin_public', models.BooleanField(default=False))
        
        # Adding field 'Profile.birthdate'
        db.add_column('core_profile', 'birthdate', models.DateTimeField(null=True, blank=True))
        
        # Adding field 'Profile.year_in_school'
        db.add_column('core_profile', 'year_in_school', models.CharField(default='Other', max_length=40))
        
        # Adding field 'Profile.address_city'
        db.add_column('core_profile', 'address_city', models.CharField(max_length=200, null=True, blank=True))
        
        # Adding field 'Profile.address'
        db.add_column('core_profile', 'address', models.CharField(max_length=200, null=True, blank=True))
        
        # Adding field 'Profile.desired_job'
        db.add_column('core_profile', 'desired_job', models.CharField(max_length=100, null=True, blank=True))
        
        # Adding field 'Profile.address_state'
        db.add_column('core_profile', 'address_state', models.CharField(max_length=40, null=True, blank=True))
        
        # Adding field 'Profile.address_zip'
        db.add_column('core_profile', 'address_zip', models.CharField(max_length=20, null=True, blank=True))
        
        # Adding field 'Profile.hometown'
        db.add_column('core_profile', 'hometown', models.CharField(max_length=100, null=True, blank=True))
        
        # Adding field 'Profile.ethnicity'
        db.add_column('core_profile', 'ethnicity', models.CharField(default='Other', max_length=40))
        
        # Adding field 'Profile.twitter_public'
        db.add_column('core_profile', 'twitter_public', models.BooleanField(default=False))
        
        # Adding field 'Profile.facebook_public'
        db.add_column('core_profile', 'facebook_public', models.BooleanField(default=False))
        
        # Adding field 'Profile.degree_area'
        db.add_column('core_profile', 'degree_area', models.CharField(default='Other', max_length=40))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Profile.linkedin_public'
        db.delete_column('core_profile', 'linkedin_public')
        
        # Deleting field 'Profile.birthdate'
        db.delete_column('core_profile', 'birthdate')
        
        # Deleting field 'Profile.year_in_school'
        db.delete_column('core_profile', 'year_in_school')
        
        # Deleting field 'Profile.address_city'
        db.delete_column('core_profile', 'address_city')
        
        # Deleting field 'Profile.address'
        db.delete_column('core_profile', 'address')
        
        # Deleting field 'Profile.desired_job'
        db.delete_column('core_profile', 'desired_job')
        
        # Deleting field 'Profile.address_state'
        db.delete_column('core_profile', 'address_state')
        
        # Deleting field 'Profile.address_zip'
        db.delete_column('core_profile', 'address_zip')
        
        # Deleting field 'Profile.hometown'
        db.delete_column('core_profile', 'hometown')
        
        # Deleting field 'Profile.ethnicity'
        db.delete_column('core_profile', 'ethnicity')
        
        # Deleting field 'Profile.twitter_public'
        db.delete_column('core_profile', 'twitter_public')
        
        # Deleting field 'Profile.facebook_public'
        db.delete_column('core_profile', 'facebook_public')
        
        # Deleting field 'Profile.degree_area'
        db.delete_column('core_profile', 'degree_area')
        
    
    
    models = {
        'core.profile': {
            'address': ('models.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'address_city': ('models.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'address_state': ('models.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'address_zip': ('models.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'bio': ('models.TextField', [], {}),
            'birthdate': ('models.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'blog_uri': ('models.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"profile_created_by"'}),
            'degree_area': ('models.CharField', [], {'default': "'Other'", 'max_length': '40'}),
            'desired_job': ('models.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ethnicity': ('models.CharField', [], {'default': "'Other'", 'max_length': '40'}),
            'facebook_public': ('models.BooleanField', [], {'default': 'False'}),
            'facebookid': ('models.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'gender': ('models.BooleanField', [], {'default': 'True'}),
            'hometown': ('models.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'linkedin_public': ('models.BooleanField', [], {'default': 'False'}),
            'linkedinid': ('models.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'phone': ('models.CharField', [], {'max_length': '25', 'blank': 'True'}),
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
