"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
>>>>>>> 94a81eb432a52582e503668e85b4cc9249584108

application = get_wsgi_application()
