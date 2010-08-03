
from south.db import db
from django.db import models
from news21national.photos.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Photo.date_taken'
        db.add_column('photos_photo', 'date_taken', models.DateTimeField(null=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Photo.date_taken'
        db.delete_column('photos_photo', 'date_taken')
        
    
    
    models = {
        'photos.gallery': {
            'Meta': {'_bases': ['news21national.multimedia.models.Media']},
            'media_ptr': ('models.OneToOneField', ["orm['multimedia.Media']"], {}),
            'photos': ('models.ManyToManyField', ["orm['photos.Photo']"], {'related_name': "'galleries'", 'null': 'True', 'blank': 'True'})
        },
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'photos.photo': {
            'Meta': {'_bases': ['news21national.multimedia.models.Media']},
            'date_taken': ('models.DateTimeField', [], {'null': 'True'}),
            'image': ('models.ForeignKey', ["orm['photos.Image']"], {}),
            'media_ptr': ('models.OneToOneField', ["orm['multimedia.Media']"], {})
        },
        'multimedia.media': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'story.story': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'photos.galleryupload': {
            'caption': ('models.TextField', ["_('caption')"], {'blank': 'True'}),
            'description': ('models.TextField', ["_('description')"], {'blank': 'True'}),
            'gallery': ('models.ForeignKey', ["orm['photos.Gallery']"], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('models.BooleanField', ["_('is public')"], {'default': 'True'}),
            'title': ('models.CharField', ["_('title')"], {'max_length': '75'}),
            'zip_file': ('models.FileField', ["_('images file (.zip)')"], {'storage': 'FileSystemStorage()'})
        },
        'photos.image': {
            'created': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'crop_horz': ('models.PositiveIntegerField', ["_('crop horizontal')"], {'default': '1'}),
            'crop_vert': ('models.PositiveIntegerField', ["_('crop vertical')"], {'default': '1'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('models.ImageField', ["_('image')"], {'max_length': '255'}),
            'modified': ('models.DateTimeField', [], {'auto_now': 'True'}),
            'view_count': ('models.PositiveIntegerField', [], {'default': '0', 'editable': 'False'})
        }
    }
    
    complete_apps = ['photos']
