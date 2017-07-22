from .settings import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '6*lrete)p@fv3u((ox4^a=q^m!y+4@+!2bx3*daht8nz3^vl+4'

DEBUG = False

ALLOWED_HOSTS = ['some.host.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR + STATIC_URL,
]

LOGGING_CONFIG = None

LOGGING = {
    'version': 2,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': ' %(asctime)s %(levelname)s %(module)s %(process)d %(thread)d %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + 'LogFile.log',
            'formatter': 'verbose'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },

    },
    'loggers': {
        '': {
            'handlers': ['file', 'null', 'console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO')
        },
    }
}

logging.config.dictConfig(LOGGING)
