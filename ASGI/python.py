# for this project you need to install "channels_redict==3.4.1" becuz it's work on this version
#################################################################################################

# asgi.py in project folder
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from APP_NAME import routing  # Import the routing file

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'YOUR_PROJECT_NAME.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns  # Use the WebSocket URL patterns
        )
    ),
})


#################################################################################################

# consumers.py in app folder
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
         await self.accept()

    async def disconnect(self, close_code):
       pass

    # Receive message from WebSocket
    async def receive(self, text_data):
        # any process when data sends from client to server
        await print(json.loads(text_data)["message"])        


    # send data to webSocket
    async def send_data(self):
        text_data = {"message" : "hello from server"}
        text_data = json.dumps(text_data) # convert dict to json format 
        
        await self.send(text_data=text_data)

#################################################################################################

# routing.py in app folder
from django.urls import path
from .consumers import * 

websocket_urlpatterns = [
    path(r'ws/SOME_FUCKING_PATH', CONSUMERS_CLASS.as_asgi()),
    
]

#################################################################################################


