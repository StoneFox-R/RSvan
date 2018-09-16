import websocket,os

socket=websocket.create_connection("ws://127.0.0.1:8080")
#socket.send('asdfasdfasdf')

while True:
    socket.send('Login')
    if input('?!')=='exit':
        os._exit(0)
    else:
        socket.send('aa')
    #print('a')

    pass
    