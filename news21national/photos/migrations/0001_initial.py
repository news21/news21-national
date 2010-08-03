
from south.db import db
from django.db import models
from news21national.photos.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Photo'
        db.create_table('photos_photo', (
            ('media_ptr', models.OneToOneField(orm['multimedia.Media'])),
            ('image', models.ForeignKey(orm.Image)),
        ))
        db.send_create_signal('photos', ['Photo'])
        
        # Adding model 'GalleryUpload'
        db.create_table('photos_galleryupload', (
            ('id', models.AutoField(primary_key=True)),
            ('zip_file', models.FileField(_('images file (.zip)'), storage=FileSystemStorage())),
            ('gallery', models.ForeignKey(orm.Gallery, null=True, blank=True)),
            ('title', models.CharField(_('title'), max_length=75)),
            ('caption', models.TextField(_('caption'), blank=True)),
            ('description', models.TextField(_('description'), blank=True)),
            ('is_public', models.BooleanField(_('is public'), default=True)),
        ))
        db.send_create_signal('photos', ['GalleryUpload'])
        
        # Adding model 'Gallery'
        db.create_table('photos_gallery', (
            ('media_ptr', models.OneToOneField(orm['multimedia.Media'])),
        ))
        db.send_create_signal('photos', ['Gallery'])
        
        # Adding model 'Image'
        db.create_table('photos_image', (
            ('id', models.AutoField(primary_key=True)),
            ('image', models.ImageField(_('image'), max_length=255)),
            ('crop_horz', models.PositiveIntegerField(_('crop horizontal'), default=1)),
            ('crop_vert', models.PositiveIntegerField(_('crop vertical'), default=1)),
            ('view_count', models.PositiveIntegerField(default=0, editable=False)),
            ('created', models.DateTimeField(auto_now_add=True)),
            ('modified', models.DateTimeField(auto_now=True)),
        ))
        db.send_create_signal('photos', ['Image'])
        
        # Adding ManyToManyField 'Gallery.photos'
        db.create_table('photos_gallery_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gallery', models.ForeignKey(orm.Gallery, null=False)),
            ('photo', models.ForeignKey(orm.Photo, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Photo'
        db.delete_table('photos_photo')
        
        # Deleting model 'GalleryUpload'
        db.delete_table('photos_galleryupload')
        
        # Deleting model 'Gallery'
        db.delete_table('photos_gallery')
        
        # Deleting model 'Image'
        db.delete_table('photos_image')
        
        # Dropping ManyToManyField 'Gallery.photos'
        db.delete_table('photos_gallery_photos')
        
    
    
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
