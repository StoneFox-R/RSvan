#
#创建人：Stone
#创建日期：2018年8月25日
#
import threading,time,threading,asyncio,os,Test
from websocket_server import WebsocketServer
maxclient=100
def NewClient(client,server):
    print (client['id'])
    client[client['id']]=Users
           
    print("New client connected and was given id %d" % client['id'])
    
def ClientLeft(client,server):
    print("Client(%d) disconnected" % client['id'])

def MessageRecv(client,server,message):
    print("Client(%d) said: %s" % (client['id'], message))
    recvmessage=message.split(' ')
    if recvmessage[0]=='Login': 
        client[client['id']].Change(Users,'Login')
        Test.BmobCloud.Login(Test,recvmessage[1],recvmessage[2])
class Users():
    state =' '
    def __init__(self):
        self.state='Null'
    def Change(self,sta):
        self.state=sta

PORT=8080

server = WebsocketServer(PORT)
server.set_fn_new_client(NewClient)
server.set_fn_client_left(ClientLeft)
server.set_fn_message_received(MessageRecv)
server.run_forever()


