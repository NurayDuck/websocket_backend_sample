from django.urls import re_path

from .consumers import PaymentConsumer

websocket_urlpatterns = [
    re_path('ws/payment_updates/', PaymentConsumer.as_asgi()),
    re_path(r'ws/payment/$', PaymentConsumer.as_asgi()),
]

