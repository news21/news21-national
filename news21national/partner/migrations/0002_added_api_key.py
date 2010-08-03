
from south.db import db
from django.db import models
from news21national.partner.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Partner.api_key'
        db.add_column('partner_partner', 'api_key', models.CharField(null=True, max_length=100, editable=False, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Partner.api_key'
        db.delete_column('partner_partner', 'api_key')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'partner.partner': {
            'api_key': ('models.CharField', [], {'null': 'True', 'max_length': '100', 'editable': 'False', 'blank': 'True'}),
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
        }
    }
    
    complete_apps = ['partner']
