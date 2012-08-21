import os


TESTS_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

SITE_ID = 1

ROOT_URLCONF = 'tests.urls'

SECRET_KEY = 'secret key'

INSTALLED_APPS = (
    'django.contrib.sites',
    'tests.test_middleware',
    'tests.test_context_processors',
    'tests.test_helpers',
)
