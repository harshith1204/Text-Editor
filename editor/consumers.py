import json
from channels.generic.websocket import AsyncWebsocketConsumer

class DocumentConsumer(AsyncWebsocketConsumer):
    active_users = {}  

    async def connect(self):
        self.room_group_name = "document_room"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        self.user_id = self.channel_name
        DocumentConsumer.active_users[self.user_id] = "Anonymous"

        await self.broadcast_active_users()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

        if self.user_id in DocumentConsumer.active_users:
            del DocumentConsumer.active_users[self.user_id]
            await self.broadcast_active_users()

    async def receive(self, text_data):
        data = json.loads(text_data)

        if "type" in data and data["type"] == "set_nickname":
            DocumentConsumer.active_users[self.user_id] = data["nickname"]
            await self.broadcast_active_users()

        if "content" in data:
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "document_update", "content": data["content"]}
            )

    async def document_update(self, event):
        await self.send(text_data=json.dumps({"content": event["content"]}))

    async def broadcast_active_users(self):
        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "active_users_update", "active_users": DocumentConsumer.active_users}
        )

    async def active_users_update(self, event):
        await self.send(text_data=json.dumps({"active_users": event["active_users"]}))
