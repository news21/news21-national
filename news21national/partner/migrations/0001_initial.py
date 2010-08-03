
from south.db import db
from django.db import models
from news21national.partner.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Partner'
        db.create_table('partner_partner', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=150)),
            ('site_url', models.URLField(verify_exists=True)),
            ('phone', models.CharField(max_length=25)),
            ('email', models.EmailField(max_length=150)),
            ('created_by', models.ForeignKey(orm['auth.User'], related_name="partner_created_by")),
            ('created_at', models.DateTimeField(editable=False)),
            ('updated_by', models.ForeignKey(orm['auth.User'], related_name="partner_updated_by")),
            ('updated_at', models.DateTimeField(editable=False)),
        ))
        db.send_create_signal('partner', ['Partner'])
        
        # Adding ManyToManyField 'Partner.members'
        db.create_table('partner_partner_members', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('partner', models.ForeignKey(orm.Partner, null=False)),
            ('user', models.ForeignKey(orm['auth.User'], null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Partner'
        db.delete_table('partner_partner')
        
        # Dropping ManyToManyField 'Partner.members'
        db.delete_table('partner_partner_members')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'partner.partner': {
            'created_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'created_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"partner_created_by"'}),
            'email': ('models.EmailField', [], {'max_length': '150'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'members': ('models.ManyToManyField', ["orm['auth.User']"], {'related_name': '"partner_members"'}),
            'name': ('models.CharField', [], {'max_length': '150'}),
            'phone': ('models.CharField', [], {'max_length': '25'}),
            'site_url': ('models.URLField', [], {'verify_exists': 'True'}),
            'updated_at': ('models.DateTimeField', [], {'editable': 'False'}),
            'updated_by': ('models.ForeignKey', ["orm['auth.User']"], {'related_name': '"partner_updated_by"'})
        }
    }
    
    complete_apps = ['partner']
