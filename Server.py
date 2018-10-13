'''
创建人：Stone
创建日期：2018年8月25日
'''
import threading,time,threading,asyncio,os,Test,Cover
from websocket_server import WebsocketServer

Useridlist=[]
def NewClient(client,server):
    print (client['id'])          
    print("New client connected and was given id %d" % client['id'])
    
def ClientLeft(client,server):
    print(client['id'])
    Useridlist.remove(client['id'])

    print("Client(%d) disconnected" % client['id'])

def MessageRecv(client,server,message):
    print("Client(%d) said: %s" % (client['id'], message))
    message=Cover.Unencryption(message)
    if Useridlist.count(client['id'])==0:
        print(message)
        recvmessage=message.split(' ')
        if recvmessage[0]=='Login': 
            if Test.BmobCloud.Login(Test,recvmessage[1],recvmessage[2])==True:
                Useridlist.append(client['id'])
                Sendmessage(client,"success")
                return
            else:
                Sendmessage(client,"PASSfail")
        else:
            if recvmessage[0]=='http':
                return
            else:
                if recvmessage[0]=='https':
                    return
                
    else:
        Sendmessage(client,"ALlogin")

def Sendmessage(client,message):
    message=Cover.Encryption(message)
    server.send_message(client,message)

PORT=os.getenv("PORT")

server = WebsocketServer(PORT)
server.set_fn_new_client(NewClient)
server.set_fn_client_left(ClientLeft)
server.set_fn_message_received(MessageRecv)
server.run_forever()


