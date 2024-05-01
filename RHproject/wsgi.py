"""
WSGI config for RHproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.handlers.wsgi import WSGIHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RHproject.settings')

# Get the Django WSGI application
django_application = get_wsgi_application()

# Wrap the Django application with WSGIHandler to conform to WSGI specification
def application(environ, start_response):
    # Pass the WSGI environment and start_response function to the Django application
    return WSGIHandler()(environ, start_response)
