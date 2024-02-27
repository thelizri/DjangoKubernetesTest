from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import async_to_sync


class ChartConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("sensor_data", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("sensor_data", self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))

    async def sensor_data(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))
