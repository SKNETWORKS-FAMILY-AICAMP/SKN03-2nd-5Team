"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
>>>>>>> a11d904d093b04032d0b0470a72aae8de1706b28

application = get_asgi_application()
