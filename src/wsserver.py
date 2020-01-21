import asyncio, websockets
from .wsmessage import Message
import json


class Server(object):

    subscribers:dict = dict()

    def __init__(self):
        pass

    async def notify(self, message:Message):
        """
        Envoyer une notification a tous les utilisateurs
        :arg message
        """
        await asyncio.wait([subscriber.send(message) for subscriber in self.subscribers])

    async def handle_message(self, websocket, path):
        """
        main function, executer a la reception d'un message
        :arg websocket
        :arg path
        """
        nom = await  websocket.recv()
        if websocket.romate_address[0] not in self.subscribers.keys():
            self.subscribers[websocket.romate_address[0]] = nom
        async for data in websocket:
            message = Message.fromJson(json.dumps(data))
            await self.notify(message)

    def run(self, host:str, port:int):
        """
        lancer le server, !important(event loop)
        :arg host address IP de l'hôte
        :arg port port d'ecoute
        """
        start_server = websockets.serve(self.handle_message, host, port)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()