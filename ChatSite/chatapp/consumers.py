# we need an asynchronous web socket consumer
# to handle the chat messages that will be sent
# from the client side to the server side.
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    # this method is called when the websocket
    # connection is established

    async def connect(self):
        # get the room name from the url route
        self.scope['url_route']['kwargs']['room_name']
        # create a room group with the room name
        self.room_group_name = 'chat_%s' % self.room_name

        # join the room group
        # as it is async we need to await

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    # this method is called when the websocket
    # connection is closed
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
