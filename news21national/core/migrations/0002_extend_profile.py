
from south.db import db
from django.db import models
from news21national.core.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'UserSkills'
        db.create_table('core_userskills', (
            ('id', models.AutoField(primary_key=True)),
            ('user', models.ForeignKey(orm['auth.User'])),
            ('skill', models.ForeignKey(orm.Skill)),
            ('sort', models.IntegerField()),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="userskill_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('core', ['UserSkills'])
        
        # Adding model 'Skill'
        db.create_table('core_skill', (
            ('id', models.AutoField(primary_key=True)),
            ('title', models.CharField(max_length=200)),
        ))
        db.send_create_signal('core', ['Skill'])
        
        # Adding model 'UserSuggestedLeads'
        db.create_table('core_usersuggestedleads', (
            ('id', models.AutoField(primary_key=True)),
            ('user', models.ForeignKey(orm['auth.User'])),
            ('oulet', models.CharField(max_length=200)),
            ('outlet_uri', models.CharField(max_length=300)),
            ('outlet_phone', models.CharField(max_length=25, blank=True)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="usersuggestedleads_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('core', ['UserSuggestedLeads'])
        
        # Adding field 'Profile.facebookid'
        db.add_column('core_profile', 'facebookid', models.CharField(max_length=200))
        
        # Adding field 'Profile.gender'
        db.add_column('core_profile', 'gender', models.BooleanField(default=True))
        
        # Adding field 'Profile.blog_uri'
        db.add_column('core_profile', 'blog_uri', models.CharField(max_length=300))
        
        # Adding field 'Profile.twitterid'
        db.add_column('core_profile', 'twitterid', models.CharField(max_length=200))
        
        # Adding field 'Profile.bio'
        db.add_column('core_profile', 'bio', models.TextField())
        
        # Adding field 'Profile.linkedinid'
        db.add_column('core_profile', 'linkedinid', models.CharField(max_length=200))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'UserSkills'
        db.delete_table('core_userskills')
        
        # Deleting model 'Skill'
        db.delete_table('core_skill')
        
        # Deleting model 'UserSuggestedLeads'
        db.delete_table('core_usersuggestedleads')
        
        # Deleting field 'Profile.facebookid'
        db.delete_column('core_profile', 'facebookid')
        
        # Deleting field 'Profile.gender'
        db.delete_column('core_profile', 'gender')
        
        # Deleting field 'Profile.blog_uri'
        db.delete_column('core_profile', 'blog_uri')
        
        # Deleting field 'Profile.twitterid'
        db.delete_column('core_profile', 'twitterid')
        
        # Deleting field 'Profile.bio'
        db.delete_column('core_profile', 'bio')
        
        # Deleting field 'Profile.linkedinid'
        db.delete_column('core_profile', 'linkedinid')
        
    
    
    models = {
        'core.profile': {
            'bio': ('models.TextField', [], {}),
            'blog_uri': ('models.CharField', [], {'max_length': '300'}),
            'facebookid': ('models.CharField', [], {'max_length': '200'}),
            'gender': ('models.BooleanField', [], {'default': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'linkedinid': ('models.CharField', [], {'max_length': '200'}),
            'phone': ('models.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'twitterid': ('models.CharField', [], {'max_length': '200'}),
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
