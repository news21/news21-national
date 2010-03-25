
import os

# NOTE: you need to create a secretkey


ADMINS = (
	# ('Your Name', 'your_email@domain.com'),
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
	'django_messages',
	'announcements',
	'mobileadmin',
	'avatar',
	'discussion',
	#
	'news21national.core',
	#
	'news21ams.newsroom',
	'news21ams.partner',
	'news21ams.story',
	'news21ams.multimedia',
	'news21ams.utils',
	'news21ams.plaintext',
	'news21ams.photos',
	'news21ams.swfs',
	'news21ams.api',
	'news21ams.audio',
	'news21ams.editorsdesk',
)

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
	os.path.join(os.path.dirname(__file__), "templates/n21alpha"),
)

SITE_NAME = "N21"
SITE_ID = 1

SITE_STYLE = 'n21alpha'

API_VERSION = 'v1'

AVATAR_STORAGE_DIR = os.path.join(os.path.dirname(__file__), 'media/avatars')

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
