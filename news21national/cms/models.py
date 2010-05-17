from django.db import models

from feincms.module.page.models import Page
from feincms.content.raw.models import RawContent
from feincms.content.image.models import ImageContent
from feincms.content.medialibrary.models import MediaFileContent
from feincms.content.contactform.models import ContactFormContent 

import mptt

Page.register_templates({
    'key': 'base',
    'title': 'Grid16 Template',
    'path': 'g16-template.html',
    'regions': (
        ('main', 'Main region'),
        ),
    })
Page.register_templates({
    'key': '12-4',
    'title': 'Grid12-4 Template',
    'path': 'g12-4-template.html',
    'regions': (
        ('main', 'Main region'),
        ('sidebar', 'Sidebar', 'inherited'),
        ),
    })
Page.create_content_type(RawContent)
Page.create_content_type(ContactFormContent)
MediaFileContent.default_create_content_type(Page)
Page.create_content_type(ImageContent, POSITION_CHOICES=(
    ('default', 'Default position'),
    ))

