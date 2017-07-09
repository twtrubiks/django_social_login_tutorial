"""
WSGI config for django_social_login_tutorial project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_social_login_tutorial.settings")
# Heroku 佈署
application = get_wsgi_application()
# application = DjangoWhiteNoise(application)


