import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import publi.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'publi.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            publi.routing.websocket_urlpatterns
        )
    ),
})
