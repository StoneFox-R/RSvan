import websocket,os,Cover

socket=websocket.create_connection("ws://127.0.0.1:8080")
#socket.send('asdfasdfasdf')

while True:

    socket.send(Cover.Encryption('Login c44455faf0 1231234569'))
    if input('?!')=='exit':
        os._exit(0)
    else:
        socket.send(Cover.Encryption('aaa'))
    #print('a')

    pass
    
