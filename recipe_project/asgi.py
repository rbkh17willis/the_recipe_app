"""
ASGI config for bookstore project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
# ASGI (Asynchronous Server Gateway Interface) is the standard for
# asynchronous communication among Python web servers, frameworks, and applications.
# The callable (anything that can be called) application is defined in this file, and it allows
# for communication between the server and your code. You won’t need to touch this file either.

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')

application = get_asgi_application()
