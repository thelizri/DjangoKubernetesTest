from django.urls import path
from .consumers import ChartConsumer

websocket_urlpatterns = [
    path("ws/chart/", ChartConsumer.as_asgi()),
]
