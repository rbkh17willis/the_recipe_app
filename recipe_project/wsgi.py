"""
WSGI config for bookstore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
# WSGI (Web Server Gateway Interface) is Python’s deployment standard for
# servers and applications. In this file, Django provides the basic configuration for serving
# your application. You also don’t need to touch this file.

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')

application = get_wsgi_application()
