
import os

# NOTE: you need to create a secretkey


ADMINS = (
	('News21', 'admin@news21.com'),
)

MANAGERS = ADMINS


DATABASE_ENGINE = 'postgresql_psycopg2'	   # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#DATABASE_NAME = ''
#DATABASE_USER = ''			   # Not used with sqlite3.
#DATABASE_PASSWORD = ''		   # Not used with sqlite3.
DATABASE_HOST = 'localhost'			   # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = ''			   # Set to empty string for default. Not used with sqlite3.


TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'


MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.middleware.doc.XViewMiddleware',
	#
	#'debug_toolbar.middleware.DebugToolbarMiddleware',
	'django_authopenid.middleware.OpenIDMiddleware',
)

ROOT_URLCONF = 'news21national.urls'


INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.gis',
	'django.contrib.admin',
	'django.contrib.sites',
	'django.contrib.markup',
	#
	'tagging',
	'south',
	'registration',
	'django_authopenid',
	'imagekit',
	'audioplayer',
	'googleanalytics',
	'googlecharts',
	'geotagging',
	'uni_form',
	'ajax_validation',
	'django_messages',
	'announcements',
	'avatar',
	'discussion',
	'debug_toolbar',
	'mptt',
	#
	'news21national.bundle',
	'news21national.core',
	'news21national.cms',
	'news21national.partner',
	'news21national.editorsdesk',
	'news21national.newsroom',
	'news21national.story',
	'news21national.multimedia',
	'news21national.utils',
	'news21national.plaintext',
	'news21national.photos',
	'news21national.swfs',
	'news21national.api',
	'news21national.audio',
	'news21national.socialchecklist',
	'news21national.coderepo',
	'news21national.videos',
	'news21national.embed',
	#
    'feincms',
	'feincms.module.page',
    'feincms.module.medialibrary',
)


COVERAGE_MODULES = ['feincms.admin.editor',
                    'feincms.admin.item_editor',
                    #'feincms.admin.splitpane_editor', # cannot be tested at the same time as the
                                                        # tree editor currently
                    'feincms.admin.tree_editor',
                    'feincms.content.application.models',
                    'feincms.content.contactform.models',
                    'feincms.content.file.models',
                    'feincms.content.image.models',
                    'feincms.content.medialibrary.models',
                    'feincms.content.raw.models',
                    'feincms.content.richtext.models',
                    'feincms.content.rss.models',
                    'feincms.content.video.models',
                    'feincms.models',
                    'feincms.module.blog.admin',
                    'feincms.module.blog.extensions.seo',
                    #'feincms.module.blog.extensions.tags', # I don't have tagging installed here...
                    'feincms.module.blog.extensions.translations',
                    'feincms.module.blog.models',
                    'feincms.module.medialibrary.admin',
                    'feincms.module.medialibrary.models',
                    'feincms.module.page.admin',
                    'feincms.module.page.extensions.changedate',
                    'feincms.module.page.extensions.datepublisher',
                    'feincms.module.page.extensions.navigation',
                    'feincms.module.page.extensions.seo',
                    'feincms.module.page.extensions.symlinks',
                    'feincms.module.page.extensions.titles',
                    'feincms.module.page.extensions.translations',
                    'feincms.module.page.models',
                    'feincms.module.page.templatetags.feincms_page_tags',
                    'feincms.settings',
                    'feincms.templatetags.applicationcontent_tags',
                    'feincms.templatetags.feincms_tags',
                    'feincms.translations',
                    'feincms.utils',
                    'feincms.utils.cleanse',
                    'feincms.views.applicationcontent',
                    'feincms.views.base',
                    'feincms.views.decorators',
                    ]
LANGUAGES = (
    ('en', 'English'),
    )

FEINCMS_ADMIN_MEDIA = '/media/feincms/'


TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
	os.path.join(os.path.dirname(__file__), "templates/n21alpha"),
)

INTERNAL_IPS = ('127.0.0.1',)
INTERCEPT_REDIRECTS = False

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)


SITE_NAME = "N21"
SITE_ID = 1

SITE_STYLE = 'n21alpha'

API_VERSION = 'v1'

AVATAR_STORAGE_DIR = 'avatars/'
AUTO_GENERATE_AVATAR_SIZES = (80,250)
AVATAR_GRAVATAR_BACKUP = False
AVATAR_DEFAULT_URL = 'templates/n21alpha/images/avatar.png'

LOGIN_URL = "/account/signin/"
LOGIN_REDIRECT_URL = '/dashboard/'
OPENID_SREG = {
	"required": ['fullname', 'country']
}

ACCOUNT_ACTIVATION_DAYS=7
EMAIL_HOST='smtp.gmail.com'
EMAIL_USE_TLS=1
EMAIL_PORT=587
EMAIL_HOST_USER='britton.halle@news21.com'
#EMAIL_HOST_PASSWORD='' # in local_settings.py

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.request',
	'django_authopenid.context_processors.authopenid',
	'mobileadmin.context_processors.user_agent',
	'announcements.context_processors.site_wide_announcements',
	'news21national.context_processors.site_style',
	#'django.contrib.csrf.middleware.CsrfMiddleware',
)


try:
	from local_settings import *
except ImportError, exp:
	pass

# Used to dynamically create .pythongoogleanalytics file on application start
# requires settings to be place in local_settings.py
# GA_CREDENTIALS_EMAIL = ''
# GA_CREDENTIALS_PSWD = ''
# GA_ACCOUNTS_PROFILES = ''
try:
	from pythongoogleanalytics_adapter import *
except ImportError, exp:
	pass
