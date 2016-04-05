"""
WSGI config for sansanxin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""


import os
import sys

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, PROJECT_DIR)

sys.path.insert(0, '/Users/liukailin/Desktop/python/sansanxin/env/lib/python3.5/site-packages/')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sansanxin.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
