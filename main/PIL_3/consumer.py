importfrom channels.generic.websocket  AsyncWebsocketConsumer
import asyncio

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Ajoutez la connexion à un groupe, par exemple, "notifications"
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Retirez la connexion du groupe "notifications" lorsqu'elle se ferme
        await self.channel_layer.group_discard("notifications", self.channel_name)
    
    # Méthode pour recevoir des notifications du serveur et les envoyer au navigateur
    async def send_notification(self, event):
        await self.send_json(event)
