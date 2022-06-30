import os
from django.urls import re_path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from transaction_app import consumers


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ocean_dev.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r'ws/notifications/(?P<room_name>\w+)/$', consumers.NotificationConsumer.as_asgi())
        ])
    ),
})
