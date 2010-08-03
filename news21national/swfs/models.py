import os
import zipfile
from zipfile import BadZipfile

from datetime import datetime

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify


from news21national.multimedia.models import Media, MediaManager

class SwfManager(MediaManager):
    pass

class Swf(Media):

    loader_swf = models.CharField(
                    max_length=255, 
                    help_text="Path to the swf used to start the flash movie.")

    width = models.CharField(
                max_length=4,
                help_text='Width of the flash swf in pixels.')

    height = models.CharField(
                max_length=4,
                help_text='Height of the flash swf in pixels.')

    flash_compat = models.CharField(
                        "Flash Compatibility",
                        choices = (
                            ('6','6'), 
                            ('7','7'), 
                            ('8','8'), 
                            ('9','9'),
                            ('10','10')),
                        max_length=5,
                        default='9',
                        help_text="Please select the lowest compatible version of Flash.")

    zip_file = models.FileField(
                    upload_to='uploads/swfs/%Y/%m/%d/',
                    storage=FileSystemStorage(),
                    help_text='Zip file containing flash swf.',
                    max_length=200)

    objects = SwfManager()
    
    def process_zipfile(self):
        """
        Extract the files into a location and match the loader.
        """

        zf = None
        workingdir = ''

    #if os.path.isfile(self.zip_file.path):
        try:
            zf = zipfile.ZipFile(self.zip_file.path)
            #import ipdb; ipdb.set_trace()
        except BadZipfile:
            self.zip_file.delete()
            raise BadZipfile, "File is not a zip file."

        workingdir = os.path.join( 
                        os.path.dirname(zf.filename), 
                        slugify(self.title))

        bad_file = zf.testzip()
        if bad_file:
            raise Exception('"%s" in the .zip archive is corrupt.' % bad_file)

        if not os.path.isdir(workingdir):
            # TODO move dir if it exists
            os.mkdir(workingdir)

        for name in zf.namelist():

            newfile = os.path.join(workingdir, name)
            
            if newfile.endswith(os.path.sep):
                if not os.path.isdir(newfile):
                    os.mkdir(newfile)

            else:
                data = zf.read(name)
                tempdata = open(newfile, "wb")
                tempdata.writelines(data)
                tempdata.close()

        zf.close()
        #print '!!!!!!!!!'
        #print 'unzipped '+str(zf)
        #print '!!!!!!!!!'


    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_loader_url(self):
        """
        Return relative URL to loader swf
        """
        return '%s/%s/%s' % (os.path.dirname(self.zip_file.url),
                                 slugify(self.title),
                                 self.loader_swf)