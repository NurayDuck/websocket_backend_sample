"""
ASGI config for books project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books.settings')

application = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from mybook.routing import websocket_urlpatterns

from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from mybook import consumers
from mybook import routing 


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path('ws/', consumers.PaymentConsumer.as_asgi()),
        
            ])
        )
    ),
})
