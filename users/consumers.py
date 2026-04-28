import json
from channels.generic.websocket import AsyncWebsocketConsumer



class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.property_id = self.scope['url_route']['kwargs']['property_id']
        self.room_group_name = f'chat_{self.property_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        sender = data['sender']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))
# ---------------------------
# VIDEO CALL CONSUMER (WebRTC Signaling)
# ---------------------------
class VideoCallConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.property_id = self.scope['url_route']['kwargs']['id']
        self.room_group_name = f'video_property_{self.property_id}'

        # Join video room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave video room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive signaling messages from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        # type can be 'offer', 'answer', 'ice-candidate'
        message_type = data.get('type')
        message_data = data.get('data')

        # Broadcast signaling data to everyone in the room except sender
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'video_signal',
                'message_type': message_type,
                'message_data': message_data,
                'sender_channel': self.channel_name
            }
        )

    # Receive signaling from room group
    async def video_signal(self, event):
        # Avoid sending back to the same client
        if self.channel_name != event['sender_channel']:
            await self.send(text_data=json.dumps({
                'type': event['message_type'],
                'data': event['message_data']
            }))