import os
import sys

import django
from django.conf import settings
from django.test.runner import DiscoverRunner

DJANGO_DEBUG = os.environ.get('DJANGO_DEBUG', 1)


EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
]
INTERNAL_APPS = [
    'django_slideshow'
]
INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

if not settings.configured:
    settings.configure(
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:"
            }
        },
        INSTALLED_APPS=INSTALLED_APPS,
        ROOT_URLCONF='django_slideshow.tests.urls',
        TEMPLATE_DIRS=(
            os.path.join(os.path.dirname(__file__), '../templates'),
        ),
    )


def main():
    if django.VERSION >= (1, 7):
        django.setup()
    runner = DiscoverRunner(failfast=True, verbosity=int(DJANGO_DEBUG))
    failures = runner.run_tests(['django_slideshow'], interactive=True)
    sys.exit(failures)

if __name__ == '__main__':
    main()
