from django.contrib import admin
from models import *

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'photo_count', )
    list_filter = ['pub_date', ]
    date_hierarchy = 'pub_date'
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('photos',)
    
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image','view_count', 'admin_thumbnail_view')
    list_per_page = 10

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'get_view_count', 'get_thumbnail_view')
    list_filter = ['pub_date', ]
    list_per_page = 10
    prepopulated_fields = {'slug': ('title',)}

    def get_view_count(self, obj):
        return obj.image.view_count
    get_view_count.short_description = 'View Count'

    def get_thumbnail_view(self, obj):
        return obj.image.admin_thumbnail_view()
    get_thumbnail_view.allow_tags = True
    get_thumbnail_view.short_description = 'Thumbnail'


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryUpload)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Image, ImageAdmin)
