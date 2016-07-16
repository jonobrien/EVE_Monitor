""" heroku settings keep changing on their doc site, just going to leave these here """

import django.conf.global_settings as DEFAULT_SETTINGS
import dj_database_url
import os




# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
WSGI_APPLICATION = 'example.wsgi.application'
SECRET_KEY = os.environ['SECRET_KEY']
ROOT_URLCONF = 'example.urls'
LANGUAGE_CODE = 'en-us'
ALLOWED_HOSTS = ['*']
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


DEBUG = True # fix templates first...


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'social.apps.django_app.default',
    'example.crest_app',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


""" templates """


## for python3/django >1.8 support added TEMPLATES dict below
# TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
#     'social.apps.django_app.context_processors.backends'
# )
# TEMPLATES = [{
#     'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [
#             os.path.join(BASE_DIR, 'templates'),
#             os.path.join(BASE_DIR, 'static'),
#         ],
#         'APP_DIRS': True,
#     'OPTIONS': {
#         'context_processors': [
#             'social.apps.django_app.context_processors.backends',
#         ]
#     }
# }]


""" auth """


# Register an application at https://developers.eveonline.com/applications
# and put your Client ID and Secret Key here. View README.md for more details.


SOCIAL_AUTH_EVEONLINE_SECRET = os.environ['EVE_DEV_SECRET']
SOCIAL_AUTH_EVEONLINE_KEY = os.environ['EVE_DEV_ID']
AUTH_USER_MODEL = 'crest_app.EveUser'
SOCIAL_AUTH_CLEAN_USERNAMES = False
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'


AUTHENTICATION_BACKENDS = (
    'social.backends.eveonline.EVEOnlineOAuth2',
)


SOCIAL_AUTH_EVEONLINE_SCOPE = [
    'publicData',
    'characterLocationRead',
    'characterAccountRead',
    'characterContactsRead',  'characterContactsWrite',
    'characterFittingsRead',  'characterFittingsWrite',
    'characterAssetsRead',
    'characterCalendarRead',
    'characterChatChannelsRead',
    'characterClonesRead',
    'characterContractsRead',
    'characterFactionalWarfareRead',
    'characterSkillsRead',
    'characterWalletRead',
    # 'fleetRead',
    # 'structureVulnUpdate' # doesn't break on sso, but doesn't seem accessible
]


SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.debug.debug',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'social.pipeline.debug.debug',
)


""" DB """


if (os.environ.get('LOCALDB')): # doesn't error out with .get()
    DATABASES = { 'default': {'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3') } }
else:
    DATABASES = {}
    DATABASES['default'] =  dj_database_url.config()


""" static files """


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

## Static files (CSS, JavaScript, Images)
## https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'


## needed for deployment `$ python manage.py collectstatic --noinput`
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
