from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
CONN_LIST=[]
class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self,message):

        self.accept()
        CONN_LIST.append(self)

    def websocket_receive(self,message):
        text=message['text']
        for conn in CONN_LIST:
            conn.send(text)


    def websocket_disconnect(self,message):
        raise StopConsumer()